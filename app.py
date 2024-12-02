import sys
import tkinter as tk
import os
import random
import platform
import pygame  # Import pygame for audio playback
import styles  # Import the styling configurations
from falling_stars import FallingStars
import win32com.client  # Import to create a shortcut for Windows


# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Load compliments from a file
import os


def get_compliments_file_path(filename='compliments_list.txt'):
    # Get the current directory of the script
    current_directory = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_directory, filename)


def get_compliments_list_path(filename='compliments_list.txt'):
    # Get the current directory of the compliments list file
    current_directory = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_directory, filename)


def create_default_compliments_file(filename='compliments_list.txt'):
    compliments_list_path = get_compliments_list_path()  # Path to the compliments list file

    # Check if the compliments list file exists
    if not os.path.exists(compliments_list_path):
        print(f"Error: {compliments_list_path} not found.")
        return  # Return or handle this error as needed

    # Read compliments from the list file
    with open(compliments_list_path, 'r', encoding='utf-8') as file:
        compliments = file.readlines()

    compliments = [compliment.strip() for compliment in compliments]  # Clean up whitespace

    # Write the compliments to the compliments_list.txt file
    compliments_file_path = get_compliments_file_path(filename)

    with open(compliments_file_path, 'w', encoding='utf-8') as file:
        for compliment in compliments:
            file.write(compliment + '\n')

    print(f"Default compliments saved to: {compliments_file_path}")


def create_default_compliments_txt(filename='compliments.txt'):
    compliments_list_path = get_compliments_list_path()  # Path to the compliments list file

    # Check if the compliments list file exists
    if not os.path.exists(compliments_list_path):
        print(f"Error: {compliments_list_path} not found.")
        return  # Return or handle this error as needed

    # Read compliments from the list file
    with open(compliments_list_path, 'r', encoding='utf-8') as file:
        compliments = file.readlines()

    compliments = [compliment.strip() for compliment in compliments]  # Clean up whitespace

    # Write the compliments to the compliments.txt file
    compliments_file_path = get_compliments_file_path(filename)

    # Create the compliments.txt file if it does not exist
    if not os.path.exists(compliments_file_path):
        with open(compliments_file_path, 'w', encoding='utf-8') as file:
            for compliment in compliments:
                file.write(compliment + '\n')

        print(f"Default compliments saved to: {compliments_file_path}")


def load_compliments(filename='compliments.txt'):
    file_path = get_compliments_file_path(filename)
    print(f"Attempting to load compliments from: {file_path}")

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return []  # Return an empty list or handle it as needed

    # Load the compliments from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        compliments = file.readlines()

    compliments = [compliment.strip() for compliment in compliments]  # Clean up whitespace
    return compliments


# Load the startup preference from a file
def load_startup_preference(filename='startup_preference.txt'):
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, filename)

    # Print the path for logging purposes
    print(f"Loading startup preference from: {file_path}")

    # Create the file with a default value if it doesn't exist
    if not os.path.exists(file_path):
        print(f"{file_path} not found. Creating with default value.")
        with open(file_path, 'w') as file:
            file.write('1')  # Default to YES

    with open(file_path, 'r') as file:
        value = int(file.read().strip())
    print(f"Loaded startup preference: {value}")
    return value


# Save the startup preference to a file
def save_startup_preference(value, filename='startup_preference.txt'):
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, filename)

    # Print the path for logging purposes
    print(f"Saving startup preference to: {file_path}")

    with open(file_path, 'w') as file:
        file.write(str(value))
    print(f"Saved startup preference: {value}")

# Get the current operating system
def get_os():
    return platform.system()


def add_to_startup_windows():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    script_path = os.path.realpath(__file__)  # Get the full path to the Python script

    # Create a .bat file instead of .lnk to avoid potential issues with Windows shortcuts
    bat_file_path = os.path.join(startup_folder, 'compliment_app.bat')

    # Get the correct Python interpreter path
    python_executable = sys.executable  # This returns the current Python interpreter being used

    # Check if the .bat file already exists; if not, create it
    if not os.path.exists(bat_file_path):
        with open(bat_file_path, 'w') as bat_file:
            # Write the command to run your Python script
            bat_file.write(f'@echo off\n"{python_executable}" "{script_path}"\n pause 0\n')

    print(f"Startup script created at: {bat_file_path}")


# Remove from startup for Windows
def remove_from_startup_windows():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    bat_file_path = os.path.join(startup_folder, 'compliment_app.bat')

    if os.path.exists(bat_file_path):
        os.remove(bat_file_path)
        print(f"Startup script removed from: {bat_file_path}")



# Manage startup setting based on slider position (1=Yes, 0=No)
def manage_startup(slider_value):
    os_name = get_os()

    if slider_value == 1:  # YES (run at startup)
        if os_name == 'Windows':
            add_to_startup_windows()
    else:  # NO (do not run at startup)
        if os_name == 'Windows':
            remove_from_startup_windows()

    # Save the preference to a file
    save_startup_preference(slider_value)


# Function to play random audio from the 'audio/' folder
def play_random_audio(folder='audio/'):
    """Play a random audio file from the specified folder."""
    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Create the full path to the audio folder
    folder_path = os.path.join(script_dir, folder)

    # List all audio files in the folder
    if os.path.exists(folder_path):  # Check if the folder exists
        audio_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav'))]

        if audio_files:
            # Select a random audio file
            random_audio = random.choice(audio_files)

            # Load and play the audio file
            pygame.mixer.music.load(os.path.join(folder_path, random_audio))
            pygame.mixer.music.play()

            print(f"Playing audio: {random_audio}")  # For debugging purposes
        else:
            print("No audio files found in the folder.")
    else:
        print(f"Audio folder not found: {folder_path}")


# Display the compliment in the window with beautiful design
def display_compliment(canvas, compliment_text):
    """Display the compliment on the canvas."""
    styles.create_compliment_label(canvas, compliment_text)


def get_star_image_path(filename='star.png'):
    # Check if the script is running in a bundled executable
    if getattr(sys, 'frozen', False):
        # If running as a bundled executable, use _MEIPASS
        return os.path.join(sys._MEIPASS, filename)
    else:
        # If running as a script, return the normal path
        return os.path.join(os.path.dirname(__file__), filename)


# Main function to run the app
def run_app():
    create_default_compliments_file()  # Ensure the compliments file is present
    create_default_compliments_txt()    # Ensure compliments.txt file is present
    compliments = load_compliments()

    if not compliments:
        print("No compliments loaded. Please ensure that compliments.txt exists.")
        return  # Exit the app or handle it appropriately

    compliment_text = random.choice(compliments)
    print(compliment_text)

    # Load startup preference
    startup_pref = load_startup_preference()

    # Play random audio
    play_random_audio()  # Call the function to play audio when displaying the compliment

    # Create the main window
    # Create the main window
    root = tk.Tk()
    root.title("Compliment App")
    root.geometry("800x600")
    root.state('zoomed')  # Maximize window
    root.configure(bg="#edaade")

    # Create a canvas for animations
    canvas = tk.Canvas(root, width=800, height=600, bg="#edaade", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Create falling star animations
    star_image_path = get_star_image_path('star.png')
    FallingStars(canvas, star_image_path)

    # Ensure canvas is rendered before calculating dimensions
    root.update()
    styles.create_compliment_label(canvas, compliment_text)  # Display compliment on canvas

    # Create the startup label above the slider
    styles.create_startup_label(root)

    # Create a CustomSlider instance with the callback function to handle changes
    custom_slider = styles.CustomSlider(root, manage_startup)
    custom_slider.set(startup_pref)  # Set the slider to the loaded preference

    # Place the custom slider below the compliment frame without extra space
    custom_slider.slider_frame.pack(pady=5)  # Ensure no extra padding

    root.mainloop()


if __name__ == '__main__':
    run_app()
