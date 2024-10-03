import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        result_label.config(text=f"BMI: {bmi}")
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        category_label.config(text=f"Category: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")


root = tk.Tk()
root.title("BMI Calculator")


tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="BMI: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

category_label = tk.Label(root, text="Category: ")
category_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
