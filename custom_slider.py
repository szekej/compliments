import tkinter as tk

# Custom slider class
class CustomSlider:
    def __init__(self, master, command_callback):
        self.master = master
        self.command_callback = command_callback

        # Create a frame for the slider
        self.slider_frame = tk.Frame(master, bg="#edaade")  # Use the same background color
        self.slider_frame.pack(pady=2)  # Reduced padding

        # Create a canvas to draw the slider
        self.canvas = tk.Canvas(self.slider_frame, width=60, height=8, bg="#edaade", highlightthickness=0)  # Smaller width and height
        self.canvas.grid(row=0, column=1)

        # Draw the rounded trough (the slider track)
        self.trough_start = 5
        self.trough_end = 55
        self.trough_height = 4  # Reduced height of the line
        self.trough_radius = self.trough_height // 2  # radius for rounded ends

        # Create two arcs for the rounded ends
        self.left_arc = self.canvas.create_arc(
            self.trough_start - self.trough_radius, 0,
            self.trough_start + self.trough_radius, 8,
            start=90, extent=180, fill="#edaade", outline="#edaade"
        )
        self.right_arc = self.canvas.create_arc(
            self.trough_end - self.trough_radius, 0,
            self.trough_end + self.trough_radius, 8,
            start=270, extent=180, fill="#edaade", outline="#edaade"
        )

        # Draw the straight line connecting the arcs
        self.trough_line = self.canvas.create_line(
            self.trough_start, 4, self.trough_end, 4,
            fill="#b76496", width=self.trough_height  # Purple color for the line
        )

        # Create the custom slider dot
        self.slider_dot = self.canvas.create_oval(0, 0, 4, 4, fill="#4B0082", outline="")  # Smaller slider dot

        # Set initial value
        self.value = 1  # Start with YES (1)

        # Bind mouse events to the slider
        self.canvas.bind("<Button-1>", self.on_click)

        # Create labels for YES and NO
        self.no_label = tk.Label(self.slider_frame, text="NO", bg="#edaade", fg="#4B0082", font=("Helvetica", 7))  # Smaller font size
        self.no_label.grid(row=1, column=0, padx=2)  # Reduced padding

        self.yes_label = tk.Label(self.slider_frame, text="YES", bg="#edaade", fg="#4B0082", font=("Helvetica", 7))  # Smaller font size
        self.yes_label.grid(row=1, column=2, padx=2)  # Reduced padding

    def on_click(self, event):
        # Determine the new value based on click position
        if event.x < 30:  # Adjusted for smaller slider
            self.set(1)  # Set to YES (1)
        else:  # If clicked on the right side
            self.set(0)  # Set to NO (0)

    def set(self, value):
        """Set the position of the slider based on the value (1 for YES, 0 for NO)."""
        self.value = value
        # Update the position of the slider dot
        x = 5 + (value * 50)  # Calculate x position based on value (0 to 50)
        self.canvas.coords(self.slider_dot, x - 4, 0, x + 4, 8)

        # Update the command callback
        self.command_callback(self.value)

    def get(self):
        """Get the current value of the slider."""
        return self.value
