# This is a part of the programme for information about the programme
import tkinter as tk
from tkinter import ttk
import webbrowser
# ANNOTATION:
# Value "name" in all tkinter functions
# navigate to the name of master window


# Link to GitHub project
def about_link():
    webbrowser.open("https://github.com/ziomciopoziomcio/TextStreamManager")


# About window
def about(name):
    about = tk.Toplevel(name)
    about.title("About")
    label = tk.Label(about, text=f"Thank you for using TextStreamManager\nan software to ...")
    label.pack(pady=2)
    link = ttk.Label(about, text="See project on GitHub", cursor="hand2", foreground="blue")
    link.pack(pady=2)
    link.bind("<Button-1>", lambda e: about_link())
    label2 = tk.Label(about, text="Created with <3 by\nziomciopoziomcio")
    label2.pack(pady=2)

# Test function
# if __name__ == '__main__':
#     main = tk.Tk()
#     about(main)
#     main.mainloop()
