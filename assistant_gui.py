import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

# ================= USER =================
USER_NAME = "Ananda Naik"

# ================= THEME =================
BG_MAIN = "#0b1220"
BG_HEADER = "#111827"
BG_CHAT = "#020617"

FG_PRIMARY = "#38bdf8"
FG_TEXT = "#e5e7eb"
FG_SUCCESS = "#22c55e"

BTN_BG = "#38bdf8"
BTN_FG = "#020617"

# ================= VOICE =================
engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ================= WEB =================
def web_open(url, msg):
    webbrowser.open(url)
    return msg

# ================= CHAT HELPERS =================
def insert_user(text):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"\n🧑 You:\n{text}\n")
    chat_box.see(tk.END)
    chat_box.config(state=tk.DISABLED)

def animated_assistant(text, delay=18):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "\n🤖 Assistant:\n")
    chat_box.config(state=tk.DISABLED)

    def type_char(i=0):
        if i < len(text):
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, text[i])
            chat_box.see(tk.END)
            chat_box.config(state=tk.DISABLED)
            chat_box.after(delay, type_char, i + 1)

    type_char()

# ================= MIC GLOW =================
def mic_glow(active=True):
    if active:
        mic_button.config(bg="#22c55e", text="🎤 Listening...")
    else:
        mic_button.config(bg=BTN_BG, text="🎤 Speak")

# ================= AI LOGIC =================
def ai_response(command):
    command = command.lower()

    commands = {
        "hello": "Hello Ananda, how are you?",
        "hi": "Hi Ananda, welcome back",
        "how are you": "I am doing great, especially with you",
        "who are you": "I am your personal AI assistant",
        "what is my name": "Your name is Ananda Naik",

        "time": lambda: "The time is " + datetime.datetime.now().strftime("%H:%M"),
        "date": lambda: "Today's date is " + datetime.datetime.now().strftime("%d %B %Y"),
        "day": lambda: "Today is " + datetime.datetime.now().strftime("%A"),

        "open google": lambda: web_open("https://www.google.com", "Opening Google"),
        "open youtube": lambda: web_open("https://www.youtube.com", "Opening YouTube"),
        "open gmail": lambda: web_open("https://mail.google.com", "Opening Gmail"),

        "motivate me": "You are capable of great things, Ananda",
        "i am stressed": "Relax Ananda, everything will be fine",
        "tell me a joke": "Why do programmers love dark mode? Because light attracts bugs",

        "exit": "exit",
        "quit": "exit",
        "bye": "exit",
    }

    for key in commands:
        if key in command:
            action = commands[key]

            if action == "exit":
                speak("Goodbye Ananda, have a great day")
                root.destroy()
                return ""

            if callable(action):
                return action()

            return action

    return "Sorry Ananda, I am still learning this command"

# ================= VOICE INPUT =================
def listen_command():
    status_label.config(text="🎤 Listening...")
    mic_glow(True)

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        status_label.config(text="🧠 Thinking...")
        command = recognizer.recognize_google(audio, language="en-in")
        insert_user(command)

        response = ai_response(command)
        if response:
            animated_assistant(response)
            speak(response)

    except:
        animated_assistant("Sorry Ananda, I didn't catch that")
        speak("Sorry Ananda, I didn't catch that")

    mic_glow(False)
    status_label.config(text="🟢 Assistant Ready")

# ================= GUI =================
root = tk.Tk()
root.title("Advanced AI Assistant – Ananda Naik")
root.geometry("560x680")
root.configure(bg=BG_MAIN)
root.resizable(False, False)

# Header
header = tk.Frame(root, bg=BG_HEADER, height=90)
header.pack(fill="x")

tk.Label(
    header,
    text="Your Personal AI Assistant",
    font=("Segoe UI", 22, "bold"),
    fg=FG_PRIMARY,
    bg=BG_HEADER
).pack(pady=(12, 0))

tk.Label(
    header,
    text=f"Welcome to your world, {USER_NAME}",
    font=("Segoe UI", 11),
    fg=FG_TEXT,
    bg=BG_HEADER
).pack()

# Chat
chat_box = scrolledtext.ScrolledText(
    root,
    width=60,
    height=24,
    font=("Consolas", 10),
    bg=BG_CHAT,
    fg=FG_TEXT,
    insertbackground=FG_TEXT,
    bd=0,
    wrap=tk.WORD
)
chat_box.pack(pady=10)
chat_box.config(state=tk.DISABLED)

# Status
status_label = tk.Label(
    root,
    text="🟢 Assistant Ready",
    font=("Segoe UI", 10),
    fg=FG_SUCCESS,
    bg=BG_MAIN
)
status_label.pack()

# Mic Button
mic_button = tk.Button(
    root,
    text="🎤 Speak",
    font=("Segoe UI", 15, "bold"),
    bg=BTN_BG,
    fg=BTN_FG,
    padx=30,
    pady=12,
    bd=0,
    cursor="hand2",
    command=listen_command
)
mic_button.pack(pady=12)

# Welcome
welcome_text = (
    f"Welcome to your world, {USER_NAME} 🌍\n"
    "Hello Ananda, how are you today?\n"
    "I am ready to assist you."
)
animated_assistant(welcome_text)
speak(welcome_text)

root.mainloop()
