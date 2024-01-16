# This is a part of the programme for handling errors
import tkinter as tk
from tkinter import ttk
import os
import webbrowser
import requests


def track_program_path():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, '../assets/data.json')
    return path


def no_config_file():
    url = "https://raw.githubusercontent.com/ziomciopoziomcio/TextStreamManager/main/assets/variables.json"
    save_path = track_program_path()
    try:
        response = requests.get(url)
        response.raise_for_status()
        save_directory = os.path.dirname(save_path)
        os.makedirs(save_directory, exist_ok=True)
        with open(save_path, 'wb') as json_file:
            json_file.write(response.content)
        return 0
    except:
        return 1


# Emergency function, would be use when app cannot start
def cannot_start():
    malfunction = tk.Tk()
    malfunction.title("Start unsuccessful")
    information = tk.Label(malfunction,
                           text=f"Unfortunately, we cannot start the programme.\nPlease, check your internet connection and try restart app.\nIf problem still exist, download new version of app.")
    information.pack(pady=2)
    link = ttk.Label(malfunction, text="Click here to see app on GitHub", cursor="hand2", foreground="blue")
    link.pack(pady=2)
    sorry = tk.Label(malfunction, text="Sorry for that problem")
    sorry.pack(pady=2)
    malfunction.mainloop()


# Test function
# if __name__ == '__main__':
#     cannot_start()
