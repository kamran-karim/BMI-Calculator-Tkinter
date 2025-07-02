import tkinter as tk

def calculate_bmi(height, weight):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

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
    from input_screen import show_input_screen  # ✅ FIXED circular import

    for widget in root.winfo_children():
        widget.destroy()

    bmi = calculate_bmi(height, weight)
    category, color = get_category(bmi)

    tk.Label(root, text=f"Your BMI is: {bmi}", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(root, text=f"Category: {category}", font=("Helvetica", 14), fg=color).pack(pady=5)

    tk.Button(root, text="Back", command=lambda: show_input_screen(root)).pack(pady=15)
