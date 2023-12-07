import tkinter as tk
import math

def draw_bow_and_arrow(event=None):
    canvas.delete("all")  # Clear the canvas

    if event and isinstance(event.width, int) and isinstance(event.height, int):
        width = int(event.width)
        height = int(event.height)
    else:
        # Set default width and height
        width = 300
        height = 300

    bow_width = min(width, height) // 2
    bow_height = bow_width * 0.8

    # Calculate the angle between the center of the canvas and the mouse pointer
    if event:
        mouse_x = event.x
        mouse_y = event.y
    else:
        mouse_x = width // 2
        mouse_y = height // 2

    dx = mouse_x - width // 2
    dy = mouse_y - height // 2
    angle = math.atan2(dy, dx)

    # Draw bow strings
    bow_string_length = bow_width * 0.6
    string_x1 = width // 2 + bow_string_length * math.cos(angle - math.pi / 2)
    string_y1 = height // 2 + bow_string_length * math.sin(angle - math.pi / 2)
    string_x2 = width // 2 + bow_string_length * math.cos(angle + math.pi / 2)
    string_y2 = height // 2 + bow_string_length * math.sin(angle + math.pi / 2)

    canvas.create_line(width // 2, height // 2, string_x1, string_y1, fill="black", width=2)
    canvas.create_line(width // 2, height // 2, string_x2, string_y2, fill="black", width=2)

    # Draw rotated bow shape
    bow_top = height // 2 - bow_height // 2
    bow_bottom = height // 2 + bow_height // 2

    # Calculate the coordinates of the rotated bow shape
    bow_points = [
        width // 2 + bow_width * math.cos(angle - math.pi / 2),
        height // 2 + bow_width * math.sin(angle - math.pi / 2),
        width // 2 + bow_width * math.cos(angle + math.pi / 2),
        height // 2 + bow_width * math.sin(angle + math.pi / 2),
        width // 2 + bow_width * 0.5 * math.cos(angle + math.pi),
        height // 2 + bow_width * 0.5 * math.sin(angle + math.pi)
    ]

    # Draw bow shape
    canvas.create_polygon(bow_points, outline="black", fill="", width=2)

    # Draw arrow
    arrow_length = bow_width * 0.6
    arrow_x_end = width // 2 + arrow_length * math.cos(angle)
    arrow_y_end = height // 2 + arrow_length * math.sin(angle)

    canvas.create_line(width // 2, height // 2, arrow_x_end, arrow_y_end, fill="black", width=2)

# Create the main window
root = tk.Tk()
root.title("Resizable Window with Bow and Arrow")

# Create a canvas to draw the bow and arrow
canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

# Bind the resize event to the draw_bow_and_arrow function
canvas.bind("<Motion>", draw_bow_and_arrow)

# Draw the initial bow and arrow
draw_bow_and_arrow()

# Start the main loop
root.mainloop()