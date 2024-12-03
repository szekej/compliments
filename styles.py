import tkinter as tk

from custom_slider import CustomSlider

BACKGROUND_COLOR = '#ffccf2'  # soft pink background
TEXT_COLOR = '#4B0082'  # purple text color
BUTTON_BG_COLOR = '#ffd1dc'  # light pink button background
TROUGH_COLOR = '#ffd1dc'  # light pink slider trough

# font configuration
LARGE_FONT = ("Helvetica", 24, "bold")
MEDIUM_FONT = ("Helvetica", 16, "bold")
SMALL_FONT = ("Helvetica", 12, "bold")


def configure_window(root):
    """Configure the main window properties."""
    root.title("Your Daily Compliment 🌸")
    root.configure(bg="#edaade")
    root.geometry("600x400")  # full-size window


def create_compliment_label(canvas, text):
    """Get the canvas width and height to calculate center position"""
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    canvas.create_text(
        canvas_width // 2,
        canvas_height // 2,
        text=text,
        fill=TEXT_COLOR,
        font=("Helvetica", 25, "bold"),
        anchor="center",
        width=500,
        justify="center"
    )


def create_startup_label(master):
    """Create a frame for the startup question label"""
    startup_label_frame = tk.Frame(master, bg="#edaade")
    startup_label_frame.pack(pady=5)

    label = tk.Label(startup_label_frame, text="Do you want me to run automatically?", bg="#edaade", fg="#4B0082",
                     font=("Helvetica", 9))
    label.pack(pady=2)


def create_startup_slider(root, command_callback):
    """Create a custom styled slider for startup toggle."""
    return CustomSlider(root, command_callback)
