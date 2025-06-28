# README.md file for 1st task of this internship
# Storror: Your Smart Voice Assistant
# Idea: Voice Assistant


Description:

For Beginners: Create a basic voice assistant that can perform simple tasks based on voice commands. Implement features like responding to "Hello" and providing predefined responses, telling the time or date, and searching the web for information based on user queries.
 This python based voice assistant responds to your voice commands using speech recognition and text-to-speech capabilities, and also includes a simple Graphical User Interface built with Tkinter.

# Features are as folows-

- It will greet the user and respond to basic commands like:
  - "hello" / "hi"
  - "time"
  - "date"
  - "open google"
  - "open youtube"
  - "search [topic]"
  - "your name"
- It provides spoken responses using `pyttsx3`.
- Logs each voice command to a `command_log.txt` file.
- The GUI interface is specially used to start voice listening.
- It also has error handling for general speech recognition issues.

# Taking a look at the tchnologies used:
- A suitable python version that supports pyaudio
- `tkinter` – for Graphical User Interface
- `speech_recognition` – to record and process voice input
- `pyttsx3` – text-to-speech engine
- `pywhatkit` – to search the queries online
- `webbrowser` – to open different websites like google and youtube
- `datetime` – to fetch the current date and time

# How to Run it

1. **Install Dependencies:**

First making sure we have a suitable python version installed. Then, install the required libraries:
```bash
pip install speechrecognition pyttsx3 pywhatkit pyaudio
# save the file as 'task1.py'

#After this, run your code on the terminal
Run the script using the command line:
   ```bash
   python task1.py

#That was all about my basic voice assistant :)