import tkinter as tk
from tkinter import BooleanVar
import random
import string

def generate_password(use_numbers=True, use_lowercase=True, use_uppercase=True, use_symbols=True, use_spaces=True):
    characters = ''
    
    if use_numbers:
        characters += string.digits
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_symbols:
        characters += string.punctuation
    if use_spaces:
        characters += ' '

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(8))
    return password

def generate_and_display_password():
    options = {
        "use_numbers": numbers_var.get(),
        "use_lowercase": lowercase_var.get(),
        "use_uppercase": uppercase_var.get(),
        "use_symbols": symbols_var.get(),
        "use_spaces": spaces_var.get(),
    }

    password = generate_password(**options)
    password_label.config(text=f"Generated Password: {password}")

window = tk.Tk()
window.title("Password Generator")

numbers_var = BooleanVar()
lowercase_var = BooleanVar()
uppercase_var = BooleanVar()
symbols_var = BooleanVar()
spaces_var = BooleanVar()

numbers_checkbox = tk.Checkbutton(window, text="Numbers", variable=numbers_var, onvalue=True, offvalue=False)
lowercase_checkbox = tk.Checkbutton(window, text="Lowercase", variable=lowercase_var, onvalue=True, offvalue=False)
uppercase_checkbox = tk.Checkbutton(window, text="Uppercase", variable=uppercase_var, onvalue=True, offvalue=False)
symbols_checkbox = tk.Checkbutton(window, text="Symbols", variable=symbols_var, onvalue=True, offvalue=False)
spaces_checkbox = tk.Checkbutton(window, text="Spaces", variable=spaces_var, onvalue=True, offvalue=False)


generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password)


password_label = tk.Label(window, text="Generated Password: ")


numbers_checkbox.grid(row=0, column=0, sticky="W")
lowercase_checkbox.grid(row=1, column=0, sticky="W")
uppercase_checkbox.grid(row=2, column=0, sticky="W")
symbols_checkbox.grid(row=3, column=0, sticky="W")
spaces_checkbox.grid(row=4, column=0, sticky="W")
generate_button.grid(row=5, column=0, pady=10)
password_label.grid(row=6, column=0, pady=10)


window.mainloop()
