import random
from PIL import Image, ImageTk

class FloatingHearts:
    """
    A class that creates and animates floating hearts on a given canvas.

    Attributes:
        canvas (tk.Canvas): The canvas where the hearts will be displayed.
        heart_image_path (str): Path to the image file for the heart.
        heart_count (int): The number of hearts to display.
        hearts (list): A list that holds references to the heart images on the canvas.
    """

    def __init__(self, canvas, heart_image_path, heart_count=10):
        """
        Initializes the FloatingHearts object with the canvas, heart image, and count.

        Args:
            canvas (tk.Canvas): The canvas to draw the hearts on.
            heart_image_path (str): Path to the image file for the heart.
            heart_count (int): Number of hearts to create (default is 10).
        """
        self.canvas = canvas
        self.heart_image = ImageTk.PhotoImage(
            Image.open(heart_image_path).resize((30, 30))
        )
        self.heart_count = heart_count
        self.hearts = []

        self.create_hearts()

    def create_hearts(self):
        """
        Creates a set of hearts at random positions on the canvas and adds them to the list.

        Each heart is placed at a random x-coordinate and a random y-coordinate
        starting from the middle to the bottom of the canvas.
        """
        for _ in range(self.heart_count):
            x = random.randint(0, self.canvas.winfo_width())
            y = random.randint(self.canvas.winfo_height() // 2, self.canvas.winfo_height())
            heart = self.canvas.create_image(x, y, image=self.heart_image, tags="heart")
            self.hearts.append(heart)

        self.animate_hearts()

    def animate_hearts(self):
        """
        Animates the hearts by moving them upwards and adding a slight horizontal drift.

        Each heart moves upwards by a random amount and drifts left or right.
        If the heart moves off the screen, it reappears at the bottom with a new random x-coordinate.
        """
        for heart in self.hearts:
            x, y = self.canvas.coords(heart)
            new_y = y - random.randint(1, 5)
            new_x = x + random.choice([-2, -1, 0, 1, 2])
            if new_y < 0:
                new_y = self.canvas.winfo_height()
                new_x = random.randint(0, self.canvas.winfo_width())
            self.canvas.coords(heart, new_x, new_y)

        self.canvas.after(50, self.animate_hearts)
