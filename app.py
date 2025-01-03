import os
import platform
import random
import sys
import tkinter as tk

import pygame

import styles
from falling_stars import FallingStars
from floating_hearts import FloatingHearts

pygame.mixer.init()


def get_compliments_file_path(filename="compliments.txt"):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def load_compliments(filename='compliments.txt'):
    file_path = get_compliments_file_path(filename)
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


def play_random_audio(folder='audio/'):
    folder_path = os.path.join(os.path.dirname(__file__), folder)

    if os.path.exists(folder_path):
        audio_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav'))]

        if audio_files:
            random_audio = random.choice(audio_files)

            try:
                pygame.mixer.music.load(os.path.join(folder_path, random_audio))
                pygame.mixer.music.play()
                print(f"Playing audio: {random_audio}")
            except Exception as e:
                print(f"Error playing audio: {e}")


def load_startup_preference(filename='startup_preference.txt'):
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, filename)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write('1')

    with open(file_path, 'r') as file:
        value = int(file.read().strip())
    return value


def save_startup_preference(value, filename='startup_preference.txt'):
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, filename)

    with open(file_path, 'w') as file:
        file.write(str(value))


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


def remove_from_startup_windows():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    bat_file_path = os.path.join(startup_folder, 'compliment_app.bat')

    if os.path.exists(bat_file_path):
        os.remove(bat_file_path)


def manage_startup(slider_value):
    os_name = get_os()

    if slider_value == 1:  # YES - run at startup
        if os_name == 'Windows':
            add_to_startup_windows()
    else:  # NO - do not run at startup
        if os_name == 'Windows':
            remove_from_startup_windows()

    save_startup_preference(slider_value)


def create_hover_effect(canvas, text, font, color, hover_color, x, y, font_size_increase=6):
    """Creates hover-able text that enlarges and becomes bold on hover."""

    initial_font_size = int(font.split()[1]) - font_size_increase
    original_font = (font.split()[0], initial_font_size)

    text_id = canvas.create_text(x, y, text=text, font=original_font, fill=color, tags="compliment")

    def on_hover():
        # change the font size and bold text on hover
        enlarged_bold_font = (
            original_font[0], initial_font_size + font_size_increase, "bold")
        canvas.itemconfig(text_id, font=enlarged_bold_font, fill=hover_color)

    def on_leave():
        # reset font size and color
        canvas.itemconfig(text_id, font=original_font, fill=color)

    canvas.tag_bind(text_id, "<Enter>", lambda event: on_hover())
    canvas.tag_bind(text_id, "<Leave>", lambda event: on_leave())


def run_app():
    compliments = load_compliments()
    if not compliments:
        print("No compliments loaded. Exiting.")
        return

    play_random_audio()

    root = tk.Tk()
    root.title("Compliment App")
    root.geometry("800x600")
    root.state('zoomed')
    root.configure(bg="#edaade")

    # frame to organize widgets
    main_frame = tk.Frame(root, bg="#edaade")
    main_frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(main_frame, bg="#edaade", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    FallingStars(canvas, "pictures/star.png")
    FloatingHearts(canvas, "pictures/heart.png", heart_count=15)

    def display_compliment():
        """Display a random compliment with hover effect (font enlargement and color change)."""
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        canvas.delete("compliment")
        compliment_text = random.choice(compliments)

        create_hover_effect(
            canvas,
            text=compliment_text,
            font="Helvetica 30 bold",
            color="#4B0082",
            hover_color="#630063",
            x=canvas_width // 2,
            y=canvas_height // 2,
            font_size_increase=6
        )

    def initialize_compliment():
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        if canvas_width > 100 and canvas_height > 100:
            display_compliment()
        else:
            root.after(100, initialize_compliment)

    initialize_compliment()
    styles.create_startup_label(main_frame)

    custom_slider = styles.CustomSlider(main_frame, manage_startup)
    startup_pref = load_startup_preference()
    custom_slider.set(startup_pref)
    custom_slider.slider_frame.pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    run_app()
