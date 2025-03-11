import tkinter as tk
from time import strftime
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")  # Adjusted size for better look
root.configure(bg='#1E1E1E')
root.resizable(False, False)

# Welcome message
welcome_label = tk.Label(root, text="Welcome to the Digital Clock App!", 
                         font=('Segoe UI', 20, 'bold'), background='#1E1E1E', 
                         foreground='#00FF7F')
welcome_label.pack(pady=(10, 0))  # Add some padding at the top

# Run the main loop
root.mainloop()