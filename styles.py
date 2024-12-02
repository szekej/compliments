import tkinter as tk
from custom_slider import CustomSlider  # Import the custom slider class

# Color Palette
BACKGROUND_COLOR = '#ffccf2'  # Soft pink background
TEXT_COLOR = '#4B0082'  # Feminine purple text color
BUTTON_BG_COLOR = '#ffd1dc'  # Light pink button background
TROUGH_COLOR = '#ffd1dc'  # Light pink slider trough

# Font Configuration
LARGE_FONT = ("Helvetica", 24, "bold")
MEDIUM_FONT = ("Helvetica", 16, "bold")
SMALL_FONT = ("Helvetica", 12, "bold")

# Window configuration
def configure_window(root):
    """Configure the main window properties."""
    root.title("Your Daily Compliment 🌸")
    root.configure(bg="#edaade")
    root.geometry("600x400")  # Full-size window

# Compliment label configuration
def create_compliment_label(canvas, text):
    # Get the canvas width and height to calculate center position
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Add the text to the center of the canvas with center alignment
    canvas.create_text(
        canvas_width // 2,  # Center horizontally
        canvas_height // 2,  # Center vertically
        text=text,
        fill=TEXT_COLOR,  # Use the defined text color
        font=("Helvetica", 25, "bold"),
        anchor="center",  # Center the text around the coordinates
        width=500,  # Limit text width for wrapping
        justify="center"  # Align the text in the center
    )


# Startup label configuration
def create_startup_label(master):
    # Create a frame for the startup question label
    startup_label_frame = tk.Frame(master, bg="#edaade")
    startup_label_frame.pack(pady=5)  # Reduced padding around the frame

    # Create the label
    label = tk.Label(startup_label_frame, text="Do you want me to run automatically?", bg="#edaade", fg="#4B0082", font=("Helvetica", 9))  # Smaller font size
    label.pack(pady=2)  # Reduced padding to the label

# Slider configuration
def create_startup_slider(root, command_callback):
    """Create a custom styled slider for startup toggle."""
    return CustomSlider(root, command_callback)  # Only create and return one instance
