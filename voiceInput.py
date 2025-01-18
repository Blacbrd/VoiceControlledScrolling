import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pyautogui
import time


# Program workflow:

# Open instagram on reels. If not logged in, throw error
# Need to unmute

# When you say stop, an alert pops up that says "You can never stop scrolling"


#Like : x1ypdohk


# Listens to specific words in sentences
def perform_action(command):

    if "scroll" in command:
        print("Scrolling action triggered!")
        pyautogui.press("down")
    
    elif "up" in command:
        print("Scrolling up")
        pyautogui.press("up")
    
    elif "pause" in command:
        print("Pausing")

        # Moves mouse to middle of the screen
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2
        pyautogui.moveTo(center_x, center_y)
        pyautogui.click()
    
    elif "like" in command:
        try:
            # Locate the like button using its class name
            like_button = driver.find_element(By.CLASS_NAME, "x1ypdohk")
            
            # Scroll into view if necessary
            driver.execute_script("arguments[0].scrollIntoView();", like_button)
            time.sleep(0.5)  # Wait a moment to ensure the button is in view
            
            # Click the like button
            like_button.click()
            print("Liked the reel!")
        except Exception as e:
            print(f"Error clicking the like button: {e}")

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
        recogniser.energy_threshold = 2000
        recogniser.dynamic_energy_threshold = True

        while True:
            try:

                # Listen to the microphone
                audio = recogniser.listen(source, phrase_time_limit=2)

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

    # Open Instagram Reels in the browser
    driver.get("https://www.instagram.com/reels")
    
    # Wait for the page to load (adjust as needed)
    time.sleep(1)
    
    # Start listening for voice commands
    listen_and_recognize()

PROFILE_PATH = r""

# Adds options to chrome path
options = Options()
options.add_argument(f"user-data-dir={PROFILE_PATH}")
options.add_argument("profile-directory=Default")

# Initialize Selenium WebDriver
driver = webdriver.Chrome(options=options)

open_instagram()