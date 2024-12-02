import os
import tkinter as tk
import random
from PIL import Image, ImageTk

class FallingStars:
    def __init__(self, canvas, star_image_path):
        self.canvas = canvas
        self.star_image = self.load_star_image(star_image_path)
        self.stars = []  # List to keep track of falling stars
        self.animate_stars()  # Start the animation

    def load_star_image(self, image_path):
        # Get the directory where the current script is located
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Create the full path to the star image
        full_image_path = os.path.join(script_dir, image_path)

        # Load and resize the star image
        if os.path.exists(full_image_path):
            image = Image.open(full_image_path).convert("RGBA")
            image = image.resize((30, 30), Image.LANCZOS)  # Resize the image
            return ImageTk.PhotoImage(image)
        else:
            print(f"Star image not found: {full_image_path}")
            return None  # Return None or handle error gracefully

    def animate_stars(self):
        # Create a new star at a random horizontal position
        star_id = self.canvas.create_image(random.randint(0, self.canvas.winfo_width()), -30, image=self.star_image)
        self.stars.append(star_id)  # Keep track of the star

        # Move the stars down the canvas
        self.move_star(star_id)
        self.canvas.after(1000, self.animate_stars)  # Create a new star every second

    def move_star(self, star_id):
        # Move the star down by 5 pixels
        self.canvas.move(star_id, 0, 5)
        x, y = self.canvas.coords(star_id)  # Get current coordinates

        # Ensure the star is always on top of other canvas items
        self.canvas.tag_raise(star_id)

        # Remove the star if it goes off the bottom of the canvas
        if y > self.canvas.winfo_height():
            self.canvas.delete(star_id)  # Remove from the canvas
            self.stars.remove(star_id)  # Remove from the list
        else:
            self.canvas.after(50, self.move_star, star_id)  # Repeat this method every 50ms
