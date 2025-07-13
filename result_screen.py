# result_screen.py
import tkinter as tk

def calculate_bmi(height, weight):
    try:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return 0.0  # Safe fallback

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight", "blue"
    elif bmi < 25:
        return "Normal", "green"
    elif bmi < 30:
        return "Overweight", "orange"
    else:
        return "Obese", "red"

def show_result_screen(root, height, weight):
    from input_screen import show_input_screen  #  Avoid circular import

    # Clear the screen
    for widget in root.winfo_children():
        widget.destroy()

    # Calculate BMI
    bmi = calculate_bmi(height, weight)
    category, color = get_category(bmi)

    # Result Labels
    tk.Label(root, text="BMI Result", font=("Helvetica", 18, "bold")).pack(pady=10)
    tk.Label(root, text=f"Your BMI is: {bmi}", font=("Helvetica", 16)).pack(pady=5)
    tk.Label(root, text=f"Category: {category}", font=("Helvetica", 14), fg=color).pack(pady=5)

    # Back button
    tk.Button(root, text="Back", font=("Helvetica", 12), command=lambda: show_input_screen(root)).pack(pady=20)

