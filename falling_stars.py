import os
import random

from PIL import Image, ImageTk


class FallingStars:
    def __init__(self, canvas, star_image_path):
        self.canvas = canvas
        self.star_image = self.load_star_image(star_image_path)
        self.stars = []
        self.animate_stars()

    def load_star_image(self, image_path):
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
        star_id = self.canvas.create_image(random.randint(0, self.canvas.winfo_width()), -30, image=self.star_image)
        self.stars.append(star_id)

        self.move_star(star_id)
        self.canvas.after(1000, self.animate_stars)

    def move_star(self, star_id):
        self.canvas.move(star_id, 0, 5)
        x, y = self.canvas.coords(star_id)

        self.canvas.tag_raise(star_id)

        if y > self.canvas.winfo_height():
            self.canvas.delete(star_id)
            self.stars.remove(star_id)
        else:
            self.canvas.after(50, self.move_star, star_id)
