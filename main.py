import tkinter as tk

def main():
    root = tk.Tk()
    root.title("BMI Calculator")
    root.geometry("400x300")

    # Lazy import to avoid circular error
    from input_screen import show_input_screen
    show_input_screen(root)

    root.mainloop()

if __name__ == "__main__":
    main()
