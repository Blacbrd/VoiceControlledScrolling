import speech_recognition as sr

#
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
        recogniser.adjust_for_ambient_noise(source)

        while True:
            try:

                # Listen to the microphone
                print("Listening...")
                audio = recogniser.listen(source)

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

listen_and_recognize()