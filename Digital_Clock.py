import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")  # Adjusted size for better look
root.configure(bg='#1E1E1E')
root.resizable(False, False)

# Run the main loop
root.mainloop()