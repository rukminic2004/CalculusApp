from tkinter import *
from sympy import *
from sympy.abc import x
import re

init_printing()

def preprocess_input(expr):
    expr = expr.replace('^', '**')
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr)
    expr = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1*\2', expr)
    expr = expr.replace("ln", "log")
    return expr

def calculate(operation):
    expr_input = entry.get()
    try:
        expr_input = preprocess_input(expr_input)
        expr = sympify(expr_input)
        if operation == "derivative":
            result = diff(expr, x)
            result_label.config(text=f"🧮 Derivative:\n{pretty(result)}")
        elif operation == "integral":
            result = integrate(expr, x)
            result_label.config(text=f"∫ Integral:\n{pretty(result)}")
    except Exception as e:
        result_label.config(text=f"❌ Error: {e}")

# GUI
root = Tk()
root.title("Derivative & Integral Calculator")
root.geometry("500x400")
root.config(bg="#f0f4ff")

Label(root, text="Enter Function (use x as variable):", font=("Arial", 14, "bold"), bg="#f0f4ff").pack(pady=10)

entry = Entry(root, font=("Arial", 16), width=30, borderwidth=3, relief="solid")
entry.pack(pady=10)

frame = Frame(root, bg="#f0f4ff")
frame.pack(pady=10)

Button(frame, text="🧮 Derivative", font=("Arial", 12), width=15, command=lambda: calculate("derivative")).grid(row=0, column=0, padx=10)
Button(frame, text="∫ Integral", font=("Arial", 12), width=15, command=lambda: calculate("integral")).grid(row=0, column=1, padx=10)

result_label = Label(root, text="", font=("Courier", 14), bg="#f0f4ff", justify=LEFT)
result_label.pack(pady=20)

root.mainloop()
