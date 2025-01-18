import speech_recognition as sr
from selenium import webdriver
import webbrowser


# Program workflow:

# Open instagram on reels. If not logged in, throw error
# Need to unmute

# When you say stop, an alert pops up that says "You can never stop scrolling"





# Listens to specific words in sentences
def perform_action(command):

    if "scroll" in command:
        print("Scrolling action triggered!")
        # Add your scrolling logic here

    elif "stop" in command:
        print("Stopping the program...")
        return False
    
    return True

def listen_and_recognize():

    # Initialises objects
    recogniser = sr.Recognizer()
    microphone = sr.Microphone()

    print("Listening for the word 'scroll'. Say 'stop' to quit.")

    # Uses microphone as main source
    with microphone as source:

        # Adjust for background noise
        recogniser.adjust_for_ambient_noise(source, duration=1)

        while True:
            try:

                # Listen to the microphone
                audio = recogniser.listen(source, phrase_time_limit=1)

                # Recognise speech and convert to lowercase
                command = recogniser.recognize_google(audio).lower()
                print(f"You said: {command}")

                # If stop is said, False is returned, therefore the while loop ends
                if not perform_action(command):
                    break
            
            # If anything goes wrong or unrecognised
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
            except sr.RequestError as e:
                print(f"Error with the recognition service: {e}")
                break

def open_instagram():

    webbrowser.open("https://www.instagram.com/reels")
    listen_and_recognize()

open_instagram()