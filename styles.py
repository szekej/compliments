import tkinter as tk
import tkinter.font as tk_font
from custom_slider import CustomSlider

BACKGROUND_COLOR = '#ffccf2'  # soft pink background
TEXT_COLOR = '#4B0082'  # purple text color
BUTTON_BG_COLOR = '#ffd1dc'  # light pink button background
TROUGH_COLOR = '#ffd1dc'  # light pink slider trough

LARGE_FONT = ("Helvetica", 24, "bold")
MEDIUM_FONT = ("Helvetica", 16, "bold")
SMALL_FONT = ("Helvetica", 12, "bold")


def configure_window(root):
    """
    Configure the main window properties.

    This function sets the title, background color, and geometry of the main window.
    The window is configured with a custom size and background color.

    Args:
        root (tk.Tk): The Tkinter root window that will be configured.
    """
    root.title("Your Daily Compliment 🌸")
    root.configure(bg="#edaade")
    root.geometry("600x400")


def wrap_text(text, font, max_width):
    """
    Wrap text to fit within the specified width.

    This function takes a string of text and splits it into multiple lines such that no line
    exceeds the maximum width specified. The width of the text is measured using the given font.

    Args:
        text (str): The string of text to be wrapped.
        font (tk_font.Font): The font object used to measure text width.
        max_width (int): The maximum width that a line of text can occupy.

    Returns:
        list: A list of lines of wrapped text.
    """
    lines = []
    words = text.split()
    current_line = []

    for word in words:
        test_line = " ".join(current_line + [word])
        test_width = font.measure(test_line)

        if test_width <= max_width:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]

    if current_line:
        lines.append(" ".join(current_line))

    return lines


def create_compliment_label(canvas, text, font=LARGE_FONT, max_width=500):
    """
    Get the canvas width and height to calculate center position and wrap text.

    This function creates a text label on the given canvas, ensuring that the text is
    wrapped appropriately to fit within the specified width. The text is centered on the canvas.

    Args:
        canvas (tk.Canvas): The canvas on which the text will be drawn.
        text (str): The compliment text to be displayed.
        font (tuple): The font configuration used for the text. Default is LARGE_FONT.
        max_width (int): The maximum width of the text. Default is 500 pixels.
    """
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    font_obj = tk_font.Font(family=font[0], size=font[1], weight=font[2])
    wrapped_text = wrap_text(text, font_obj, max_width)
    final_text = "\n".join(wrapped_text)

    canvas.create_text(
        canvas_width // 2,
        canvas_height // 2,
        text=final_text,
        fill=TEXT_COLOR,
        font=font_obj,
        anchor="center",
        width=max_width,
        justify="center",
        tags="compliment"
    )


def create_startup_label(master):
    """
    Create a frame for the startup question label.

    This function creates a label asking the user if they want the application to
    run automatically at startup. The label is placed inside a frame and is added
    to the provided master widget.

    Args:
        master (tk.Widget): The parent widget where the label frame will be placed.
    """
    startup_label_frame = tk.Frame(master, bg="#edaade")
    startup_label_frame.pack(pady=5)

    label = tk.Label(startup_label_frame, text="Do you want me to run automatically?", bg="#edaade", fg="#4B0082",
                     font=("Helvetica", 9))
    label.pack(pady=2)


def create_startup_slider(root, command_callback):
    """
    Create a custom styled slider for startup toggle.

    This function creates a slider that allows the user to toggle whether the
    application should run at startup. The slider is styled according to the
    application's theme and is linked to the provided callback function.

    Args:
        root (tk.Widget): The parent widget where the slider will be placed.
        command_callback (function): The callback function to be called when the slider value changes.

    Returns:
        CustomSlider: The custom styled slider widget.
    """
    return CustomSlider(root, command_callback)
