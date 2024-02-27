import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("PythonExamples.org")

# Maximize window
window.state("zoomed")

label = tk.Label(window, text="Hello World!")
label.pack()

# Run the application
window.mainloop()