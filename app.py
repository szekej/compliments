import os
import platform
import random
import sys
import tkinter as tk

import pygame

import styles
from falling_stars import FallingStars

pygame.mixer.init()


def get_compliments_file_path(filename="compliments_list.txt"):
    """Get the current directory of the script"""
    current_directory = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_directory, filename)


def get_compliments_list_path(filename='compliments_list.txt'):
    """Get the current directory of the compliments list file"""
    current_directory = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_directory, filename)


def create_default_compliments_file(filename='compliments_list.txt'):
    compliments_list_path = get_compliments_list_path()

    if not os.path.exists(compliments_list_path):
        print(f"Error: {compliments_list_path} not found.")
        return

    with open(compliments_list_path, 'r', encoding='utf-8') as file:
        compliments = file.readlines()

    compliments = [compliment.strip() for compliment in compliments]

    compliments_file_path = get_compliments_file_path(filename)

    with open(compliments_file_path, 'w', encoding='utf-8') as file:
        for compliment in compliments:
            file.write(compliment + '\n')

    print(f"Default compliments saved to: {compliments_file_path}")


def create_default_compliments_txt(filename='compliments.txt'):
    compliments_list_path = get_compliments_list_path()

    if not os.path.exists(compliments_list_path):
        print(f"Error: {compliments_list_path} not found.")
        return

    with open(compliments_list_path, 'r', encoding='utf-8') as file:
        compliments = file.readlines()

    compliments = [compliment.strip() for compliment in compliments]

    compliments_file_path = get_compliments_file_path(filename)

    if not os.path.exists(compliments_file_path):
        with open(compliments_file_path, 'w', encoding='utf-8') as file:
            for compliment in compliments:
                file.write(compliment + '\n')

        print(f"Default compliments saved to: {compliments_file_path}")


def load_compliments(filename='compliments.txt'):
    file_path = get_compliments_file_path(filename)
    print(f"Attempting to load compliments from: {file_path}")

    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        compliments = file.readlines()

    compliments = [compliment.strip() for compliment in compliments]
    return compliments


def load_startup_preference(filename='startup_preference.txt'):
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, filename)

    print(f"Loading startup preference from: {file_path}")

    if not os.path.exists(file_path):
        print(f"{file_path} not found. Creating with default value.")
        with open(file_path, 'w') as file:
            file.write('1')

    with open(file_path, 'r') as file:
        value = int(file.read().strip())
    print(f"Loaded startup preference: {value}")
    return value


def save_startup_preference(value, filename='startup_preference.txt'):
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, filename)

    print(f"Saving startup preference to: {file_path}")

    with open(file_path, 'w') as file:
        file.write(str(value))
    print(f"Saved startup preference: {value}")


def get_os():
    return platform.system()


def add_to_startup_windows():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    script_path = os.path.realpath(__file__)

    bat_file_path = os.path.join(startup_folder, 'compliment_app.bat')

    python_executable = sys.executable

    if not os.path.exists(bat_file_path):
        with open(bat_file_path, 'w') as bat_file:
            bat_file.write(f'@echo off\n"{python_executable}" "{script_path}"\n pause 0\n')

    print(f"Startup script created at: {bat_file_path}")


def remove_from_startup_windows():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    bat_file_path = os.path.join(startup_folder, 'compliment_app.bat')

    if os.path.exists(bat_file_path):
        os.remove(bat_file_path)
        print(f"Startup script removed from: {bat_file_path}")


def manage_startup(slider_value):
    os_name = get_os()

    if slider_value == 1:  # YES (run at startup)
        if os_name == 'Windows':
            add_to_startup_windows()
    else:  # NO (do not run at startup)
        if os_name == 'Windows':
            remove_from_startup_windows()

    save_startup_preference(slider_value)


def play_random_audio(folder='audio/'):
    """Play a random audio file from the specified folder."""
    script_dir = os.path.dirname(os.path.realpath(__file__))

    folder_path = os.path.join(script_dir, folder)

    if os.path.exists(folder_path):
        audio_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav'))]

        if audio_files:
            random_audio = random.choice(audio_files)

            pygame.mixer.music.load(os.path.join(folder_path, random_audio))
            pygame.mixer.music.play()

            print(f"Playing audio: {random_audio}")
        else:
            print("No audio files found in the folder.")
    else:
        print(f"Audio folder not found: {folder_path}")


def display_compliment(canvas, compliment_text):
    """Display the compliment on the canvas."""
    styles.create_compliment_label(canvas, compliment_text)


def get_star_image_path(filename='star.png'):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return os.path.join(os.path.dirname(__file__), filename)


def run_app():
    create_default_compliments_file()
    create_default_compliments_txt()
    compliments = load_compliments()

    if not compliments:
        print("No compliments loaded. Please ensure that compliments.txt exists.")
        return

    compliment_text = random.choice(compliments)
    print(compliment_text)

    startup_pref = load_startup_preference()

    play_random_audio()

    root = tk.Tk()
    root.title("Compliment App")
    root.geometry("800x600")
    root.state('zoomed')
    root.configure(bg="#edaade")

    canvas = tk.Canvas(root, width=800, height=600, bg="#edaade", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    star_image_path = get_star_image_path('star.png')
    FallingStars(canvas, star_image_path)

    root.update()
    styles.create_compliment_label(canvas, compliment_text)

    styles.create_startup_label(root)

    custom_slider = styles.CustomSlider(root, manage_startup)
    custom_slider.set(startup_pref)

    custom_slider.slider_frame.pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    run_app()
