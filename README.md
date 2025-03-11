
# 🕒 Digital Clock using Tkinter  

This is a simple **Digital Clock** created using Python's `tkinter` library. It displays the current time in **24-hour format** and updates automatically every second.

---

## 🚀 Features  
✅ Real-time clock with 24-hour format  
✅ Modern UI with rounded frame and custom colors  
✅ Easy to use and modify  

---


## 📂 Project Structure  
```
📁 DigitalClock  
├── README.md  
├── Digital_Clock.py  
├── f1.txt  
└── f2.txt  
```

---

## 🛠️ Requirements  
- Python 3.x  

---

## 📥 Installation  
1. Clone the repository:  
```bash  
git clone https://github.com/SaiTejaSalvaji/DigitalClock.git  
```  
2. Navigate to the project folder:  
```bash  
cd DigitalClock  
```  
3. Run the program:  
```bash  
python Digital_Clock.py  
```  

---

## 📃 Code Explanation  
### ➡️ `update_time()`  
- Uses `strftime()` to fetch the current time in **HH:MM:SS** format.  
- Updates the label every second using `after()` function.  

### ➡️ UI Design  
- `tk.Frame` creates a rounded frame for the clock display.  
- `tk.Label` displays the time with custom font and color.  
- `root.mainloop()` starts the main event loop.  

---

## 🎨 Customization  
- **Background color** – Modify `bg='#1E1E1E'` in `root.configure()`  
- **Font and size** – Adjust `font=('Segoe UI', 50, 'bold')` in `label`  
- **Text color** – Change `foreground='#00FFFF'` in `label`  

---

## 📄 License  
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  

---

## 🙌 Acknowledgments  
💖 Created with Python and Tkinter  

---

Feel free to modify and enhance the project! 😎  
```
