import tkinter as tk
import sqlite3
from result_screen import show_result_screen

# Connect to SQLite database
conn = sqlite3.connect("bmi_app_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    height_cm REAL,
    weight_kg REAL,
    bmi REAL,
    category TEXT
)
""")
conn.commit()

def show_input_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Enter Name").pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Enter Height (cm)").pack(pady=5)
    height_entry = tk.Entry(root)
    height_entry.pack()

    tk.Label(root, text="Enter Weight (kg)").pack(pady=5)
    weight_entry = tk.Entry(root)
    weight_entry.pack()

    info_label = tk.Label(root, text="", fg="red")
    info_label.pack()

    def calculate_bmi(height, weight):
        height_m = height / 100
        return round(weight / (height_m ** 2), 2)

    def get_category(bmi):
        if bmi < 18.5:
            return "Underweight", "blue"
        elif bmi < 25:
            return "Normal", "green"
        elif bmi < 30:
            return "Overweight", "orange"
        else:
            return "Obese", "red"

    def on_calculate():
        try:
            name = name_entry.get().strip()
            height = float(height_entry.get())
            weight = float(weight_entry.get())

            if not name or height <= 0 or weight <= 0:
                raise ValueError

            bmi = calculate_bmi(height, weight)
            category, _ = get_category(bmi)

            # Save to database
            cursor.execute("INSERT INTO bmi_data (name, height_cm, weight_kg, bmi, category) VALUES (?, ?, ?, ?, ?)",
                           (name, height, weight, bmi, category))
            conn.commit()

            show_result_screen(root, height, weight)
        except ValueError:
            info_label.config(text="Please enter a valid name, height and weight.")

    def show_records():
        cursor.execute("SELECT name, height_cm, weight_kg, bmi, category FROM bmi_data")
        records = cursor.fetchall()

        if not records:

            
            tk.messagebox.showinfo("No Data", "No records found.")
            return

        data_window = tk.Toplevel(root)
        data_window.title("Saved BMI Records")
        data_window.geometry("650x400")
        data_window.config(bg="white")

        frame = tk.Frame(data_window)
        frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(frame, bg="white")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        table_frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=table_frame, anchor="nw")

        headers = ["Name", "Height", "Weight", "BMI", "Category"]
        for col_num, col in enumerate(headers):
            tk.Label(table_frame, text=col, bg="#dcdcdc", font=("Arial", 10, "bold"),
                     borderwidth=1, relief="solid", width=15).grid(row=0, column=col_num)

        for row_num, row in enumerate(records, start=1):
            for col_num, val in enumerate(row):
                tk.Label(table_frame, text=val, borderwidth=1, relief="solid", width=15).grid(row=row_num, column=col_num)

    tk.Button(root, text="Calculate BMI", command=on_calculate, bg="#4CAF50", fg="white").pack(pady=10)
    tk.Button(root, text="Show Records", command=show_records, bg="#2196F3", fg="white").pack(pady=5)
