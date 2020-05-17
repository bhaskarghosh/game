from tkinter import *
import ast
import random
import time, threading
from threading import Thread
import sys, select


# Define our fake command
def fake_command():
    pass


def hide(my_frame):
    my_frame.grid_forget()


def show(my_frame):
    my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


def load_level_shape_info():
    with open("level_shape.txt", "r") as fp:
        contents = fp.read()
        shape_game["level_shape"] = ast.literal_eval(contents)


def load_guide():
    with open("instrguide.txt", "r") as fp:
        shape_game["instr_guide"] = fp.read()


def next_shape():
    print("In Next Shape " + time.ctime())
    r_key = random.choices(shape_game["keylist"])
    return shape_game["shape_map"][r_key[0]]


def load_shapesdb():
    with open("shapesdb.txt", "r") as fp:
        contents = fp.read()
        shape_game["shape_map"] = ast.literal_eval(contents)
    shape_game["keylist"] = list(shape_game["shape_map"].keys())


def create_menus(root):

    # Define a Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Create Menu Items
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=fake_command)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # Create another submenu Edit
    edit_menu = Menu(my_menu)
    my_menu.add_cascade(label="Help", menu=edit_menu)
    edit_menu.add_command(label="Shapes Help", command=fake_command)
    edit_menu.add_separator()
    edit_menu.add_command(label="About", command=fake_command)


root = Tk()
root.title("Recognize the Shape")
root.geometry("800x800")
root.iconbitmap("c:/guis/codemy.ico")
create_menus(root)

# show_button = Button(root, text="Show", command=show)
# hide_button = Button(root, text="Hide", command=hide)

# show_button.grid(row=0, column=0)
# hide_button.grid(row=0, column=1)

# my_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
# my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

# frame_label = Label(my_frame, text="Hello World!", font=("Helvetica", 20))
# frame_label.pack(padx=20, pady=20)

root.mainloop()
