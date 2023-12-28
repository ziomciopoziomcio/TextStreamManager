import requests
import tkinter as tk
from tkinter import ttk
import webbrowser

# ANNOTATION:
# Value "name" in all tkinter functions
# navigate to the name of master window

running_version = "genesis-1.0.0"


def update_link():
    webbrowser.open("https://github.com/ziomciopoziomcio/TextStreamManager/releases")


# Function to download name of latest version
def version_download():
    try:
        response = requests.get(
            "https://raw.githubusercontent.com/ziomciopoziomcio/TextStreamManager/main/assets/version.txt")
        if response.status_code == 200:
            return response.text
        else:
            return -1
    except:
        return -1


# Notification when update is available
def new_version(name, current, new):
    updater = tk.Toplevel(name)
    updater.title("New version available")
    label = tk.Label(updater, text=f"You are currently running old version:\n{current}\nThe latest version:\n{new}")
    label.pack(pady=2)
    link = ttk.Label(updater, text="Click here to see releases", cursor="hand2", foreground="blue")
    link.pack(pady=2)
    link.bind("<Button-1>", lambda e: update_link())
    updater.mainloop()


# Notification when user uses the newest version
def uptodate(name, current):
    updater = tk.Toplevel(name)
    updater.title("Up to date")
    label = tk.Label(updater, text=f"You are currently running the latest version:\n{current}")
    label.pack(pady=10)
    updater.mainloop()


# Notification when data is unavailable
def error(name):
    updater = tk.Toplevel(name)
    updater.title("Error")
    label = tk.Label(updater, text="We cannot download the latest version.\nCheck your internet connection")
    label.pack(pady=10)
    updater.mainloop()


# # Brain of update system
def update_controller(name):
    downloaded_version = version_download()
    if downloaded_version == -1:
        error(name)
    elif downloaded_version == running_version:
        uptodate(name, running_version)
    else:
        new_version(name, running_version, downloaded_version)


# Test function
# if __name__ == '__main__':
#     main = tk.Tk()
#     update_controller(main)
#     main.mainloop()
