import tkinter as tk


class CustomSlider:
    def __init__(self, master, command_callback):
        self.master = master
        self.command_callback = command_callback

        self.slider_frame = tk.Frame(master, bg="#edaade")
        self.slider_frame.pack(pady=2)

        self.canvas = tk.Canvas(self.slider_frame, width=60, height=8, bg="#edaade", highlightthickness=0)
        self.canvas.grid(row=0, column=1)

        self.trough_start = 5
        self.trough_end = 55
        self.trough_height = 4
        self.trough_radius = self.trough_height // 2

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

        self.trough_line = self.canvas.create_line(
            self.trough_start, 4, self.trough_end, 4,
            fill="#b76496", width=self.trough_height
        )

        self.slider_dot = self.canvas.create_oval(0, 0, 4, 4, fill="#4B0082", outline="")

        self.value = 1  # start with YES (1)

        self.canvas.bind("<Button-1>", self.on_click)

        self.no_label = tk.Label(self.slider_frame, text="NO", bg="#edaade", fg="#4B0082", font=("Helvetica", 7))
        self.no_label.grid(row=1, column=0, padx=2)

        self.yes_label = tk.Label(self.slider_frame, text="YES", bg="#edaade", fg="#4B0082", font=("Helvetica", 7))
        self.yes_label.grid(row=1, column=2, padx=2)

    def on_click(self, event):
        if event.x < 30:
            self.set(1)  # YES
        else:
            self.set(0)  # NO

    def set(self, value):
        """Set the position of the slider based on the value (1 for YES, 0 for NO)."""
        self.value = value
        x = 5 + (value * 50)
        self.canvas.coords(self.slider_dot, x - 4, 0, x + 4, 8)

        self.command_callback(self.value)

    def get(self):
        """Get the current value of the slider."""
        return self.value
