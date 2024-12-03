import os
import random
from PIL import Image, ImageTk

class FallingStars:
    """
    A class that creates and animates falling stars on a given canvas.

    Attributes:
        canvas (tk.Canvas): The canvas where the stars will be displayed.
        star_image_path (str): Path to the image file for the star.
        stars (list): A list that holds references to the stars on the canvas.
    """

    def __init__(self, canvas, star_image_path):
        """
        Initializes the FallingStars object with the canvas and star image.

        Args:
            canvas (tk.Canvas): The canvas to draw the stars on.
            star_image_path (str): Path to the image file for the star.
        """
        self.canvas = canvas
        self.star_image = self.load_star_image(star_image_path)
        self.stars = []

        self.animate_stars()

    def load_star_image(self, image_path):
        """
        Loads and resizes the star image from the provided path.

        Args:
            image_path (str): Path to the image file for the star.

        Returns:
            ImageTk.PhotoImage: The resized image to be used on the canvas, or None if the image cannot be found.
        """
        script_dir = os.path.dirname(os.path.realpath(__file__))
        full_image_path = os.path.join(script_dir, image_path)

        if os.path.exists(full_image_path):
            image = Image.open(full_image_path).convert("RGBA")
            image = image.resize((30, 30), Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        else:
            print(f"Star image not found: {full_image_path}")
            return None

    def animate_stars(self):
        """
        Creates and animates a falling star.

        A star is created at a random x-coordinate, and it falls down the canvas.
        Once it falls off the screen, it is deleted and removed from the stars list.
        The animation repeats by calling this function every second.
        """
        star_id = self.canvas.create_image(random.randint(0, self.canvas.winfo_width()), -30, image=self.star_image)
        self.stars.append(star_id)

        self.move_star(star_id)
        self.canvas.after(1000, self.animate_stars)

    def move_star(self, star_id):
        """
        Moves the specified star down the canvas.

        The star moves by 5 pixels on each call, and if it moves off the screen,
        it is deleted and removed from the stars list. Otherwise, it continues moving
        by calling this function every 50 milliseconds.

        Args:
            star_id (str): The ID of the star to be moved.
        """
        self.canvas.move(star_id, 0, 5)
        x, y = self.canvas.coords(star_id)

        self.canvas.tag_raise(star_id)

        if y > self.canvas.winfo_height():
            self.canvas.delete(star_id)
            self.stars.remove(star_id)
        else:
            self.canvas.after(50, self.move_star, star_id)
