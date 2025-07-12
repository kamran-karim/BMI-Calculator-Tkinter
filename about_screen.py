import tkinter as tk

def show_about_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="BMI Calculator App", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text="Made by Team XYZ\nCS Department, 2025\nOpen Source Project").pack(pady=10)

    tk.Button(root, text="Back", command=root.destroy).pack(pady=10)
#test changes