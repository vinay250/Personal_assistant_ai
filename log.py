# logic.py

import datetime
import webbrowser

# Optional: import speak if you want voice inside logic
# from voice import speak


# ================= WEB =================
def web_open(url, message):
    webbrowser.open(url)
    return message


# ================= AI RESPONSE =================
def ai_response(command, user_name="Ananda Naik", root=None):
    command = command.lower().strip()

    commands = {
        # Greetings
        "hello": f"Hello {user_name}, how are you?",
        "hi": f"Hi {user_name}, welcome back",
        "how are you": f"I am doing great, especially with you {user_name}",
        "who are you": "I am your personal AI assistant",
        "what is my name": f"Your name is {user_name}",

        # Time & Date
        "time": lambda: "The time is " + datetime.datetime.now().strftime("%H:%M"),
        "date": lambda: "Today's date is " + datetime.datetime.now().strftime("%d %B %Y"),
        "day": lambda: "Today is " + datetime.datetime.now().strftime("%A"),

        # Web
        "open google": lambda: web_open("https://www.google.com", "Opening Google"),
        "open youtube": lambda: web_open("https://www.youtube.com", "Opening YouTube"),
        "open gmail": lambda: web_open("https://mail.google.com", "Opening Gmail"),

        # Fun
        "motivate me": f"You are capable of great things, {user_name}",
        "i am stressed": f"Relax {user_name}, everything will be fine",
        "tell me a joke": "Why do programmers love dark mode? Because light attracts bugs",

        # Exit
        "exit": "exit",
        "quit": "exit",
        "bye": "exit",
    }

    # Matching logic
    for key in commands:
        if key in command:
            action = commands[key]

            # Exit handling
            if action == "exit":
                # If GUI exists, close it
                if root:
                    root.destroy()
                return "Goodbye! Have a great day."

            # Execute function if callable
            if callable(action):
                try:
                    return action()
                except Exception as e:
                    return f"Error: {str(e)}"

            return action

    # Default response
    return f"Sorry {user_name}, I am still learning this command."