import requests
import datetime
import random

QUOTES = [
    "Discipline is knowing you could procrastinate — and doing it anyway, just more efficiently.",
    "You don’t need to be perfect. Just be better than yesterday’s version that binge-watched YouTube.",
    "Success is mostly just showing up... and occasionally reading the instructions.",
    "Every master was once a disaster. So technically, you're just in the pre-legend phase.",
    "Progress is progress, even if it’s measured in microwaved leftovers and half-finished to-do lists.",
    "Do it tired. Do it awkward. Do it imperfect. But yeah, do it.",
    "Motivation is fleeting. Coffee is consistent. Choose wisely.",
    "You’re not behind. You’re just fashionably late to your own greatness.",
    "If you’re not failing occasionally, you’re probably just playing life on tutorial mode.",
    "Self-doubt called. I told it you were busy being kinda awesome.",
    "Today’s vibe: low energy, high potential.",
    "Remember: Even your slowest progress still outruns anyone who didn’t start.",
    "You don’t have to feel like doing it. You just have to do it anyway.",
    "Being average at something consistently is still more powerful than being amazing once.",
    "If you’ve made it this far, odds are you’ll survive the rest too.",
    "Don't not..."
]

REMINDERS = [
    "🧘 Did you meditate today?",
    "💪 Mini push-ups, squats, and sit-ups — checked off?",
]

def get_quote():
    return random.choice(QUOTES)

def get_reminder():
    return random.choice(REMINDERS)

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    quote = get_quote()
    reminder = get_reminder()

    new_log = [
        "<!--DAILY-LOG-->\n",
        f">_{quote}_\n",
        f"> 📅 Last updated: `{now}`\n",
        "<!--END-LOG-->\n"
    ]

    with open("README.md", "r", encoding="utf-8") as file:
        lines = file.readlines()

    start_index = None
    end_index = None

    for i, line in enumerate(lines):
        if line.strip() == "<!--DAILY-LOG-->":
            start_index = i
        elif line.strip() == "<!--END-LOG-->":
            end_index = i

    if start_index is not None and end_index is not None and end_index > start_index:
        updated_lines = lines[:start_index] + new_log + lines[end_index+1:]
        with open("README.md", "w", encoding="utf-8") as file:
            file.writelines(updated_lines)
    else:
        print("Markers not found or improperly ordered.")

if __name__ == "__main__":
    main()
