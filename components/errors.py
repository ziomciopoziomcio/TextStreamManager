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
