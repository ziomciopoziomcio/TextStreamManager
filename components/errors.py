import tkinter as tk
from tkinter import ttk
import webbrowser
import requests

def no_config_file():
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses

        # Ensure the save directory exists
        save_directory = os.path.dirname(save_path)
        os.makedirs(save_directory, exist_ok=True)

        # Save the content to a local file
        with open(save_path, 'wb') as json_file:
            json_file.write(response.content)

        print(f"File downloaded and saved to {save_path}")
        return 0
    except:
        return 1