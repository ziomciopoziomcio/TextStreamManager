# this is the main file of the programme

import tkinter as tk
from components import updater, about, data_reader
import json

# Function to handle menu item clicks
def on_menu_click(menu_category, menu_item):
    menu_item_id = menu_item_data.get((menu_category, menu_item), "Unknown ID")
    if menu_item_id == "Text_New":
        pass
    elif menu_item_id == "Text_Edit":
        pass
    elif menu_item_id == "Text_Save":
        pass
    elif menu_item_id == "Text_Delete":
        pass
    elif menu_item_id == "Templates_Save":
        pass
    elif menu_item_id == "Templates_Save to file":
        pass
    elif menu_item_id == "Templates_Load from file":
        pass
    elif menu_item_id == "Templates_Load from database":
        pass
    elif menu_item_id == "Help_About":
        about.about(main)
    elif menu_item_id == "Help_Check for updates":
        updater.update_controller(main)

# Check is config file exist
config_path = data_reader.variable_path()

# Create the menu window
main = tk.Tk()
main.title("TextStreamManager")

# Create a Menu widget
menu = tk.Menu(main)

# Define the menu items
menu_items = [
    ("Text", [
        ("New", "Ctrl+N"),
        ("Edit", "Ctrl+E"),
        ("Save", "Ctrl+S"),
        ("Delete", "Ctrl+Q")
    ]),
    ("Templates", [
        ("Save", "Ctrl+T"),
        ("Save to file", "Ctrl+Y"),
        ("Load from file", "Ctrl+F"),
        ("Load from database", "Ctrl+D")
    ]),
    ("Help", [
        ("About", None),
        ("Check for updates", None)
    ])
]

# Create a dictionary to store menu item IDs
menu_item_data = {}
for i, (menu_label, items) in enumerate(menu_items):
    submenu = tk.Menu(menu, tearoff=0)
    for j, (item_label, shortcut) in enumerate(items):
        submenu.add_command(label=item_label, accelerator=shortcut, command=lambda item=item_label, category=menu_label: on_menu_click(category, item))
        menu_item_data[(menu_label, item_label)] = f"{menu_label}_{item_label}"
    menu.add_cascade(label=menu_label, menu=submenu)
    main.grid_columnconfigure(i, weight=1)

# Attach the menu to the main window
main.config(menu=menu)

# Start the app
main.mainloop()
