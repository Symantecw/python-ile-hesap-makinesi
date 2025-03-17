import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Bilimsel Hesap Makinesi")
        self.root.geometry("400x600")
        
        self.equation = ""
        self.entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('sqrt', 5, 1), ('^', 5, 2), ('log', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('pi', 6, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 15), width=5, height=2, 
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
        
    def on_button_click(self, char):
        if char == 'C':
            self.equation = ""
        elif char == '=':
            try:
                self.equation = str(eval(self.equation))
            except Exception as e:
                messagebox.showerror("Hata", "Geçersiz işlem")
                self.equation = ""
        elif char == 'sqrt':
            try:
                self.equation = str(math.sqrt(float(self.equation)))
            except Exception:
                messagebox.showerror("Hata", "Geçersiz işlem")
                self.equation = ""
        elif char == '^':
            self.equation += "**"
        elif char == 'log':
            try:
                self.equation = str(math.log10(float(self.equation)))
            except Exception:
                messagebox.showerror("Hata", "Geçersiz işlem")
                self.equation = ""
        elif char == 'sin':
            self.equation = str(math.sin(math.radians(float(self.equation))))
        elif char == 'cos':
            self.equation = str(math.cos(math.radians(float(self.equation))))
        elif char == 'tan':
            self.equation = str(math.tan(math.radians(float(self.equation))))
        elif char == 'pi':
            self.equation += str(math.pi)
        else:
            self.equation += char
        
        self.update_entry()
    
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.equation)
        
if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
