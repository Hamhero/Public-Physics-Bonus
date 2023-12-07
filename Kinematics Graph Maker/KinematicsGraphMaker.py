import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def generate_graphs():
    try:
        initial_position = float(entry_initial_position.get())
        initial_velocity = float(entry_initial_velocity.get())
        acceleration = float(entry_acceleration.get())
        time_interval = float(entry_time_interval.get())
        time_end = float(entry_time_end.get())
    except ValueError:
        result_label.config(text="Please enter valid numerical values.")
        return

    time_values = np.arange(0, time_end + time_interval, time_interval)
    position_values = initial_position + initial_velocity * time_values + 0.5 * acceleration * time_values**2
    velocity_values = initial_velocity + acceleration * time_values
    acceleration_values = np.full_like(time_values, acceleration)

    ax.cla()
    ax.plot(time_values, position_values, label='Position')
    ax.plot(time_values, velocity_values, label='Velocity')
    ax.plot(time_values, acceleration_values, label='Acceleration')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    canvas.draw()

    result_label.config(text="Graphs generated successfully.")

def save_graphs():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        fig.savefig(file_path)
        result_label.config(text=f"Graphs saved successfully to {file_path}.")

root = tk.Tk()
root.title("Kinematics Graph Maker")

label_initial_position = ttk.Label(root, text="Initial Position:")
label_initial_position.grid(row=0, column=0, padx=10, pady=10)
entry_initial_position = ttk.Entry(root)
entry_initial_position.grid(row=0, column=1, padx=10, pady=10)

label_initial_velocity = ttk.Label(root, text="Initial Velocity:")
label_initial_velocity.grid(row=1, column=0, padx=10, pady=10)
entry_initial_velocity = ttk.Entry(root)
entry_initial_velocity.grid(row=1, column=1, padx=10, pady=10)

label_acceleration = ttk.Label(root, text="Acceleration:")
label_acceleration.grid(row=2, column=0, padx=10, pady=10)
entry_acceleration = ttk.Entry(root)
entry_acceleration.grid(row=2, column=1, padx=10, pady=10)

label_time_interval = ttk.Label(root, text="Time Interval:")
label_time_interval.grid(row=3, column=0, padx=10, pady=10)
entry_time_interval = ttk.Entry(root)
entry_time_interval.grid(row=3, column=1, padx=10, pady=10)

label_time_end = ttk.Label(root, text="End Time:")
label_time_end.grid(row=4, column=0, padx=10, pady=10)
entry_time_end = ttk.Entry(root)
entry_time_end.grid(row=4, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Graphs", command=generate_graphs)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Button to save graphs
save_button = ttk.Button(root, text="Save Graphs", command=save_graphs)
save_button.grid(row=7, column=0, columnspan=2, pady=10)

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=2, rowspan=8, padx=10, pady=10)

root.mainloop()
