import requests
import datetime
import random

QUOTES = [
    "Discipline is choosing between what you want now and what you want most.",
    "The man who moves a mountain begins by carrying away small stones.",
    "You won’t always be motivated. You must learn to be disciplined.",
    "You are not behind. You are exactly where you need to be.",
    "Do it tired. Do it imperfect. Just do it.",
    "Every day is a chance to get 1% better.",
]

REMINDERS = [
    "🧘 Did you meditate today?",
    "🎤 Have you done your voice training?",
    "💪 Mini push-ups, squats, and sit-ups — checked off?",
    "🎯 OSRS goal progress update: what’s the next milestone?",
]

def get_quote():
    return random.choice(QUOTES)

def get_reminder():
    return random.choice(REMINDERS)

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    quote = get_quote()
    reminder = get_reminder()

    with open("README.md", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("README.md", "w", encoding="utf-8") as file:
        for line in lines:
            if line.startswith("<!--DAILY-LOG-->"):
                file.write("<!--DAILY-LOG-->\n")
                file.write(f"> 🧠 **Quote**: _{quote}_\n")
                file.write(f"> 🔁 **Reminder**: {reminder}\n")
                file.write(f"> 📅 Last updated: `{now}`\n\n")
            else:
                file.write(line)

if __name__ == "__main__":
    main()
