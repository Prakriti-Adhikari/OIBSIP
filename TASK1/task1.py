#importing the variours libraries which are required in our code.
import tkinter as tk
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser

# Initializing the text-to-speech engine
text_to_speech_engine = pyttsx3.init()
#creating necessary functions using def.
def speakout_loud(yourmessage):
    """Convert the text message to speech"""
    text_to_speech_engine.say(yourmessage)
    text_to_speech_engine.runAndWait()
#using the datetime library functions:

def get_current_time():
    return datetime.datetime.now().strftime('%I:%M %p')

def get_current_date():
    return datetime.datetime.now().strftime('%B %d, %Y')

def process_voice_command(command):
    """Respond to recognized voice commands"""
    command = command.lower()
    response = ""

    if "hello" in command or "hi" in command:
        response = "Hello my dear user . How can I help you today?"
    elif "time" in command:
        response = f"The current time is {get_current_time()}"
    elif "date" in command:
        response = f"The Date of today is {get_current_date()}"
    elif "search" in command:
        topic = command.replace("search", "").strip()
        response = f"Searching for {topic}"
        pywhatkit.search(topic)
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        response = "Okay my dear user ! Opening Google"
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        response = "Okay my dear user! Opening youtube"
    elif "your name" in command:
        response = "My name is Storror .I'm your voice assistant."
    else:
        response = "Sorry, I didn't got that. Try saying it the other way."

    log_command(command)
    speakout_loud(response)
    label_output.config(text=response)

def listen_and_respond():
    """It is used to listen to the user's voice and handle the command efficiently."""
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            label_output.config(text=" Listening...")
            recognizer.adjust_for_ambient_noise(source)
            voice = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(voice)
            label_output.config(text=f" You said: {command}")
            process_voice_command(command)
    except sr.WaitTimeoutError:   #Handling the timeout error
        label_output.config(text="Sorry it's Timeout, please try speaking again.")
    except sr.UnknownValueError:  #Handling the unknown value error
        label_output.config(text=" Sorry my user ,I could not understand that.")
    except sr.RequestError:  #Using this to request the user to check other things
        label_output.config(text="Please check your internet connection.")

def log_command(command):
    """Log recognized command to a text file"""
    with open("command_log.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - {command}\n")

# GUI setup for an efficient code with visuals:)
root = tk.Tk()
root.title("My Smart and Cool Voice Assistant")
root.geometry("500x300")
root.configure(bg="#1e272e")

label_title = tk.Label(root, text=" Storror: Your Voice Assistant", font=("Helvetica", 20, "bold"), bg="#1a1403", fg="white")
label_title.pack(pady=20)

btn_listen = tk.Button(root, text="Start and Ask", font=("Helvetica", 14), bg="#b91e73", fg="white", command=listen_and_respond)
btn_listen.pack(pady=10)

label_output = tk.Label(root, text="", font=("Helvetica", 12), bg="#1e272e", fg="#b3bcc5", wraplength=400)
label_output.pack(pady=20)

root.mainloop()
