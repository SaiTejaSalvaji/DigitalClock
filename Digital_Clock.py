import tkinter as tk
from time import strftime
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")  # Adjusted size for better look
root.configure(bg='#1E1E1E')
root.resizable(False, False)

# Function to update time
def update_time():
    time_string = strftime('%H:%M:%S')  # 24-hour format
    label.config(text=time_string)
    label.after(1000, update_time)

# Create a Frame for rounded corners
frame = tk.Frame(root, bg='#2C2F33', bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor='center', width=460, height=120)

# Styling the clock display
label = tk.Label(frame, font=('Segoe UI', 50, 'bold'), background='#2C2F33', foreground='#00FFFF')
label.place(relx=0.5, rely=0.5, anchor='center')

# Start updating time
update_time()

# Run the main loop
root.mainloop()