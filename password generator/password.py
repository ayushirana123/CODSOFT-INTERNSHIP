import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")  # Set background color

        self.custom_font = ("Helvetica", 16)

        self.label = tk.Label(root, text="Password Generator", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        self.label.pack(pady=20)

        self.option_frame = tk.Frame(root, bg="#f0f0f0")
        self.option_frame.pack()

        self.option_label = tk.Label(self.option_frame, text="Select Password Strength:", font=self.custom_font, bg="#f0f0f0")
        self.option_label.pack(side=tk.LEFT, padx=10)

        self.options = ["Strong", "Average", "Weak"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])

        self.option_menu = tk.OptionMenu(self.option_frame, self.selected_option, *self.options)
        self.option_menu.config(font=self.custom_font)
        self.option_menu.pack(side=tk.LEFT, padx=10)

        self.password_label = tk.Label(root, text="Generated Password:", font=self.custom_font, bg="#f0f0f0")
        self.password_label.pack(pady=10)

        self.generated_password = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.generated_password, font=("Courier", 14), state="readonly")
        self.password_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", font=self.custom_font, command=self.generate_password)
        self.generate_button.pack(pady=20)

    def generate_password(self):
        password_length = 12
        password_strength = self.selected_option.get()

        if password_strength == "Strong":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif password_strength == "Average":
            characters = string.ascii_letters + string.digits
        else:
            characters = string.ascii_lowercase

        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        self.generated_password.set(generated_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
