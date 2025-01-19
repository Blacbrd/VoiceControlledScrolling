import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pyautogui
import time


# Program workflow:

# Mouse position: (1789, 986)

# Open instagram on reels. If not logged in, throw error
# Need to unmute

# When you say stop, an alert pops up that says "You can never stop scrolling"


#Like : x1lliihq x1n2onr6 xyb1xck

def locate_active_reel():
    """Locate the currently active reel container."""
    try:
        # Locate the visible reel container
        reel_container = driver.find_element(By.XPATH, "//div[@aria-hidden='false']")
        print("Active reel located.")
        return reel_container
    except Exception as e:
        print(f"Error locating active reel: {e}")
        return None

def click_like_button():
    """Click the like button within the active reel."""
    try:
        # Locate the active reel
        active_reel = locate_active_reel()

        if not active_reel:
            print("No active reel found.")
            return

        # Find the "like" button within the active reel
        like_button = active_reel.find_element(By.XPATH, ".//svg[@aria-label='Like']")
        
        # Ensure the button is visible and interactable
        if like_button.is_displayed():
            like_button.click()
            print("Liked the current reel!")
        else:
            print("Like button is not visible.")
    except Exception as e:
        print(f"Error clicking the like button: {e}")



# Listens to specific words in sentences
def perform_action(command):

    if "scroll" in command or "stroll" in command or "troll" in command:
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
        print("Liking the current reel...")
        # click_like_button()
        # Temp solution
        pyautogui.moveTo(1789, 986)
        pyautogui.click()

    
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

    # This unmutes the reels
    pyautogui.moveTo(1693, 292)
    pyautogui.click()
    
    # Start listening for voice commands
    listen_and_recognize()

PROFILE_PATH = r"C:\Users\blacb\AppData\Local\Google\Chrome\User Data"

# Adds options to chrome path
options = Options()
options.add_argument(f"user-data-dir={PROFILE_PATH}")
options.add_argument("profile-directory=Default")

# Initialize Selenium WebDriver
driver = webdriver.Chrome(options=options)

open_instagram()