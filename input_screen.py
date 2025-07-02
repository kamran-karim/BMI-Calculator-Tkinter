import tkinter as tk
from result_screen import show_result_screen

def show_input_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Enter Height (cm)").pack(pady=5)
    height_entry = tk.Entry(root)
    height_entry.pack()

    tk.Label(root, text="Enter Weight (kg)").pack(pady=5)
    weight_entry = tk.Entry(root)
    weight_entry.pack()

    def on_calculate():
        try:
            height = float(height_entry.get())
            weight = float(weight_entry.get())
            show_result_screen(root, height, weight)
        except:
            tk.Label(root, text="Invalid input!", fg="red").pack()

    tk.Button(root, text="Calculate BMI", command=on_calculate).pack(pady=10)
