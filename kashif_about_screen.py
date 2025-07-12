import tkinter as tk

def show_about_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="About This App", font=("Helvetica", 18, "bold")).pack(pady=15)

    info_text = (
        "BMI Calculator App\n"
        "Created by Team XYZ\n"
        "CS Department, 2025\n"
        "This is an Open Source Project"
    )
    tk.Label(root, text=info_text, font=("Helvetica", 12), justify="center").pack(pady=10)

    tk.Button(root, text="Back", font=("Helvetica", 10), command=root.destroy).pack(pady=20)
