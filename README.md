# 🗣️ DeskBot - AI ChatBot

A very minimal, lightweight desktop chat UI that **connects to a simple text-generation API endpoint**; using **[Pollinations.AI](https://github.com/pollinations/pollinations/blob/main/APIDOCS.md)**.

Built with [CustomTkinter](https://customtkinter.tomschimansky.com/) for an easy-to-use interface and a small ChatBot module to manage conversation state and commands.

---

## Features
- 🗨️ Modern desktop chat interface (CustomTkinter)
- ⚙️ **Simple commands:**
  - `/m: [motive]` - set bot personality/motive
  - `/r` - reset conversation history
  - `/help` - show available commands
- 🧾 Conversation history with a configurable message limit
- 🔓 Run & Go - No API Key required

---

## Quick Start

**Requirements**
- Python 3.8+
- pip

**Install dependencies:**
```bash
pip install customtkinter requests
```

**Run the app:**
```bash
python main.py
```

Or simply right-click, and _open with Python_.

---

## Usage
- Type messages in the entry box and press Enter or click Send.
- Example commands:
```text
/m: friendly guy
/r
/help
```
- The UI shows "Bot is currently thinking..." while awaiting a response.

---

## Where to configure
- API endpoint: `...\Folder\modules\bot.py` - change `self.api_url` to point to another text-generation endpoint.
- Conversation length: `max_history_messages` in ChatBot controls how many messages are kept.

---

## Project structure
- `main.py` - GUI and messaging logic
- `modules/bot.py` - ChatBot class, Prompt constructor, API caller
- `README.md` - this file

---

## Notes & Tips
- The bot respects built-in restrictions in the prompt; modify carefully if you change prompt composition.
- Increase `timeout` in `requests.get` if you face slow responses.
- The app is intentionally minimal - adapt the prompt or UI to your needs.
- If you want to make it executable, head to [PyInstaller's Documentation](https://pyinstaller.org/en/stable/).

---

## Other
**This is basically a prototype**, and I'm not expecting to update it any further, for you to change or edit.

This is my first ever project I've posted here! If you've found this cool or even useful a like (star) and follow would be nice. I also make [Roblox Modules](https://github.com/J4KEWasNotHere/Modules/tree/main), for others to use - go check it out!
