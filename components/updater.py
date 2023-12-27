import requests
import tkinter as tk


# Function to download name of latest version
def version_download():
    try:
        response = requests.get(
            "https://raw.githubusercontent.com/ziomciopoziomcio/TextStreamManager/main/assets/version.txt")
        if response == 200:
            return response.text
        else:
            return -1
    except:
        return -1


# Notification when update is available
def new_version(current, new):
    updater = tk.Tk()
    updater.title("New version available")
    label = tk.Label(updater, text="You currently running old version!")
    label.pack(pady=10)
    updater.mainloop()
# # Notification when user uses the newest version
# def uptodate(current):
#
# # Notification when data is unavailable
# def error():
#
# # Brain of update system
# def update_controller():
