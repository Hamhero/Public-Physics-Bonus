import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

class FreeBodyDiagramApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Free Body Diagram Creator")

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<Button-1>", self.start_erase)
        self.canvas.bind("<B1-ButtonRelease>", self.stop_erase)

        self.erase_button = tk.Button(self.master, text="Erase", command=self.enable_erase)
        self.erase_button.pack(side=tk.LEFT)

        self.undo_button = tk.Button(self.master, text="Undo", command=self.undo)
        self.undo_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self.master, text="Save as Image", command=self.save_as_image)
        self.save_button.pack(side=tk.LEFT)

        self.drawn_objects = []
        self.undone_objects = []
        self.erase_start = None
        self.erasing = False

    def draw_line(self, event):
        if not self.erasing:
            x, y = event.x, event.y
            dot = self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")  # Draw a small dot
            self.drawn_objects.append(("oval", dot, self.canvas.coords(dot)))
            self.undone_objects = []  # Clear the undone objects when a new action is performed

    def start_erase(self, event):
        if self.erasing:
            self.erase_start = (event.x, event.y)

    def stop_erase(self, event):
        if self.erasing and self.erase_start:
            x, y = event.x, event.y
            items = self.canvas.find_enclosed(self.erase_start[0], self.erase_start[1], x, y)
            for item in items:
                if item in [obj[1] for obj in self.drawn_objects]:
                    self.undone_objects.append(("delete", item))
                    self.canvas.delete(item)
            self.erase_start = None

    def enable_erase(self):
        self.erasing = not self.erasing

    def undo(self):
        if self.drawn_objects:
            action = self.drawn_objects.pop()
            if action[0] == "oval":
                _, dot, coords = action
                self.undone_objects.append(("delete", dot))
                self.canvas.delete(dot)
            elif action[0] == "delete":
                _, item = action
                coords = self.canvas.coords(item)
                dot = self.canvas.create_oval(coords, fill="black")
                self.undone_objects.append(("oval", dot, coords))

    def save_as_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            image = Image.new("RGB", (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), "white")
            draw = ImageDraw.Draw(image)
            for _, item, coords in self.drawn_objects:
                if _ == "oval":
                    draw.ellipse(coords, fill="black")
            image.save(file_path, format="PNG")

    def clear_canvas(self):
        for _, item, _ in self.drawn_objects:
            self.canvas.delete(item)
        self.drawn_objects = []
        self.undone_objects = []

if __name__ == "__main__":
    root = tk.Tk()
    app = FreeBodyDiagramApp(root)
    root.mainloop()
