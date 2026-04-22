# logic.py

import datetime
import webbrowser
from voice import speak

def web_open(url, msg):
    webbrowser.open(url)
    return msg

def ai_response(command, root=None):
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
    }

    for key in commands:
        if key in command:
            action = commands[key]

            if action == "exit":
                speak("Goodbye Ananda")
                if root:
                    root.destroy()
                return ""

            return action() if callable(action) else action

    return "Sorry Ananda, I am still learning this command"