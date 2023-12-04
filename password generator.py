import tkinter as tk
import random
import string
import pyperclip  # Import pyperclip for copying to clipboard

# Function to generate an easy password (digits only)
def generate_easy_password():
    length = password_length.get()
    password = ''.join(random.choices(string.digits, k=length))
    display_generated_password(password, "Easy")

# Function to generate a medium password (letters and digits)
def generate_medium_password():
    length = password_length.get()
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    display_generated_password(password, "Medium")

# Function to generate a hard password (letters, digits, and punctuation)
def generate_hard_password():
    length = password_length.get()
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    display_generated_password(password, "Hard")

# Function to display the generated password in the text widget
def display_generated_password(password, complexity):
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, f"Here's a generated '{complexity}' password for you.: \n{password}")
    password_display.config(state=tk.DISABLED)

    # Enable the copy button
    copy_button.config(state=tk.NORMAL)
    # Store the generated password in a global variable
    global generated_password
    generated_password = password

# Function to copy the generated password to the clipboard
def copy_password():
    pyperclip.copy(generated_password)

# Creating the main window
root = tk.Tk()
root.iconbitmap("password generator.ico")
root.title("Password Generator")
root.config(bg="black")  # Set background color to black

# Set the default font for the entire application to Arial
root.option_add("*Font", "Arial")

# Creating a label for the slider
length_label = tk.Label(root, text="Select Password Length:", bg="black", fg="white", font=("Arial", 12))
length_label.pack()

# Creating a scale/slider for selecting password length
password_length = tk.Scale(root, from_=4, to=40, orient=tk.HORIZONTAL, length=300, bg="black", fg="white", troughcolor="black", highlightbackground="black")
password_length.pack()

# Creating buttons for different complexity levels
easy_button = tk.Button(root, text="Generate Easy Password", command=generate_easy_password, font=("Arial", 12), bg="#C0C0C0", padx=10)
easy_button.pack(pady=5)

medium_button = tk.Button(root, text="Generate Medium Password", command=generate_medium_password, font=("Arial", 12), bg="#C0C0C0", padx=10)
medium_button.pack(pady=5)

hard_button = tk.Button(root, text="Generate Hard Password", command=generate_hard_password, font=("Arial", 12), bg="#C0C0C0", padx=10)
hard_button.pack(pady=5)

# Creating a text widget to display the generated password
password_display = tk.Text(root, height=10, width=40, font=("Arial", 12), bg="black", fg="white")
password_display.config(state=tk.DISABLED)
password_display.pack()

# Creating button to copy the generated password
copy_button = tk.Button(root, text="Copy Password", command=copy_password, font=("Arial", 12), state=tk.DISABLED)
copy_button.pack(pady=5)

# Starting the main loop
root.mainloop()
