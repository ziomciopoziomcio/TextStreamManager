# import dependencies
import tkinter as tk

# Create the menu window
main = tk.Tk()
main.title("TextStreamManager")


# Create a menu
menu = tk.Menu(main)
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

for i, (menu_label, items) in enumerate(menu_items):
    submenu = tk.Menu(menu, tearoff=0)
    for j, (item_label, shortcut) in enumerate(items):
        submenu.add_command(label=item_label, accelerator=shortcut)
    menu.add_cascade(label=menu_label, menu=submenu)
    main.grid_columnconfigure(i, weight=1)
# Start the app
main.config(menu=menu)
main.mainloop()