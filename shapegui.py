from tkinter import *
from tkinter import messagebox
import ast
import random
import time, threading
from threading import Thread
import sys, select
from PIL import ImageTk, Image

shape_game = {}
answer = ""


def Showhelp():
    response = messagebox.showinfo("How to play the Game", shape_game["instr_guide"])


# Define our fake command
def fake_command():
    pass


def game_loop():
    shape_game["completed"] = True


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
    ci = shape_game["current_image"]
    # if ci != -1:
    #     shape_game["c_label"].destroy()
    ci = random.choices(shape_game["keylist"])[0]
    print("In Next Shape " + str(ci))
    shape_game["c_label"] = Label(image=shape_game["image_map"][ci])
    # shape_game["image_map"][k] = Label(image=my_image)
    shape_game["c_label"].pack()
    shape_game["current_image"] = ci
    shape_game["status_message"].set(
        "Showing "
        + shape_game["shape_map"][ci]
        + " Image. You have "
        + str(shape_game["interval"])
        + " seconds to answer"
    )
    shape_game["c_label"].after(shape_game["interval"], check_result)

    print("return from next shape")


def load_shapesdb():
    with open("shapesdb.txt", "r") as fp:
        contents = fp.read()
        shape_game["shape_map"] = ast.literal_eval(contents)
    for k, v in shape_game["shape_map"].items():
        shape_game["image_map"][k] = ImageTk.PhotoImage(Image.open(v))
    shape_game["keylist"] = list(shape_game["shape_map"].keys())


def show_status():
    shape_game["status_message"] = StringVar()
    shape_game["status_message"].set("Ready to Play!!")
    my_status = Label(
        shape_game["root"],
        textvariable=shape_game["status_message"],
        bd=1,
        bg="#eeeeee",
        width=90,
        font="Helvetica",
        relief="sunken",
        anchor=W,
    )
    my_status.pack(side=BOTTOM, fill=X)


def check_result():
    shape_game["status_message"].set("Correct!!")


def play_the_game():
    level = shape_game["current_level"]
    i = 0
    # threading.Timer(1, try_loop).start()
    while i < int(shape_game["level_shape"][level]):
        next_shape()
        # print("i am here")
        # shape_game["entry"].after(shape_game["interval"], check_result)
        # print("after delay")
        # time.sleep(2)
        i = i + 1


def create_menus(root):

    # Define a Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Create Menu Items
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=next_shape)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # Create another submenu Edit
    edit_menu = Menu(my_menu)
    my_menu.add_cascade(label="Help", menu=edit_menu)
    edit_menu.add_command(label="Shapes Help", command=Showhelp)
    edit_menu.add_separator()
    edit_menu.add_command(label="About", command=fake_command)


def driver():
    root = Tk()
    root.title("Recognize the Shape")
    root.geometry("800x800")
    root.iconbitmap("c:/guis/codemy.ico")
    shape_game["root"] = root
    create_menus(root)
    default_level = 1
    shape_game["completed"] = False
    shape_game["image_map"] = {}

    user_suffix = str(random.randrange(0, 101, 2))
    shape_game["user"] = "user" + user_suffix

    load_guide()
    load_level_shape_info()
    how_many = int(shape_game["level_shape"][default_level])
    shape_game["interval"] = int((60 / how_many) * 1000)
    print(shape_game["interval"])
    show_status()
    load_shapesdb()
    shape_game["current_image"] = -1
    shape_game["current_level"] = 1

    shape_game["entry"] = Entry(root)
    shape_game["entry"].pack(side=BOTTOM, fill=X)
    b = Button(root, text="Start Game", command=play_the_game)
    b.pack()
    # show_button = Button(root, text="Show", command=show)
    # hide_button = Button(root, text="Hide", command=hide)

    # show_button.grid(row=0, column=0)
    # hide_button.grid(row=0, column=1)

    # my_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
    # my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

    # frame_label = Label(my_frame, text="Hello World!", font=("Helvetica", 20))
    # frame_label.pack(padx=20, pady=20)

    # image_label.pack_forget()

    root.mainloop()


if __name__ == "__main__":
    driver()
