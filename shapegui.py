from tkinter import *
from tkinter import messagebox
import ast
import random
import time, threading
from threading import Thread
import sys, select
from PIL import ImageTk, Image
import tkinter.font as font

shape_game = {}
answer = ""


def Showhelp():
    response = messagebox.showinfo("How to play the Game", shape_game["instr_guide"])


def ShowScore():
    score = "Right: " + str(shape_game["score"]["right"]) + "\n"
    score += "Wrong: " + str(shape_game["score"]["wrong"]) + "\n"

    response = messagebox.showinfo("Your Score", score)


# Define our fake command
def about_command():
    response = messagebox.showinfo(
        "AP - Computer Science Principles", shape_game["about"]
    )


def load_level_shape_info():
    with open("level_shape.txt", "r") as fp:
        contents = fp.read()
        shape_game["level_shape"] = ast.literal_eval(contents)


def load_guide():
    with open("instrguide.txt", "r") as fp:
        shape_game["instr_guide"] = fp.read()
    with open("about.txt", "r") as fp:
        shape_game["about"] = fp.read()


def check_answer(ci):
    shape_game["c_label"].destroy()
    ans = shape_game["entry"].get()
    if ans == str(ci):
        shape_game["status_message"].set("Correct!!")
        shape_game["score"]["right"] += 1
    else:
        shape_game["status_message"].set("Wrong!!")
        shape_game["score"]["wrong"] += 1
    ans = shape_game["entry"].delete(0, END)
    print(shape_game["score"])


def end_game():
    shape_game["c_label"].destroy()
    ShowScore()
    shape_game["current_level"] += 1
    if shape_game["current_level"] <= 5:
        level = shape_game["current_level"]
        shape_game["current_image"] = -1
        how_many = int(shape_game["level_shape"][level])
        shape_game["interval"] = int((60 / how_many) * 1000)
        print("Interval:" + str(shape_game["interval"]))
        shape_game["start_button"] = Button(
            shape_game["root"],
            text="Re-Start Game",
            highlightbackground="#b4ff8b",
            command=next_shape,
        )
        shape_game["start_button"]["font"] = shape_game["font"]
        shape_game["start_button"].pack(side=BOTTOM, fill=X)
    else:
        messagebox.showinfo("Game Over", "You have played all levels")


def next_shape():
    shape_game["status_message"].set("")
    if shape_game["start_button"]:
        shape_game["start_button"].destroy()
        shape_game["start_button"] = None
    level = shape_game["current_level"]
    if shape_game["counter"] >= int(shape_game["level_shape"][level]):
        end_game()
        return
    ci = shape_game["current_image"]
    if ci != -1:
        check_answer(ci)
    ci = random.choices(shape_game["keylist"])[0]
    print("In Next Shape " + str(ci))
    shape_game["c_label"] = Label(image=shape_game["image_map"][ci])
    shape_game["c_label"].pack()
    shape_game["current_image"] = ci
    shape_game["counter"] += 1
    shape_game["root"].after(shape_game["interval"], next_shape)


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
    edit_menu.add_command(label="About", command=about_command)


def init():
    shape_game["completed"] = False
    shape_game["image_map"] = {}
    user_suffix = str(random.randrange(0, 101, 2))
    shape_game["user"] = "user" + user_suffix
    shape_game["current_image"] = -1
    shape_game["current_level"] = 1
    shape_game["c_label"] = ""
    shape_game["score"] = {}
    shape_game["score"]["right"] = 0
    shape_game["score"]["wrong"] = 0
    shape_game["counter"] = 0


def driver():
    init()
    root = Tk()
    root.title("Recognize the Shape")
    root.geometry("800x800")

    shape_game["root"] = root
    create_menus(root)
    default_level = 1
    load_guide()
    load_level_shape_info()
    how_many = int(shape_game["level_shape"][default_level])
    shape_game["interval"] = int((60 / how_many) * 1000)
    print("Interval:" + str(shape_game["interval"]))
    show_status()
    load_shapesdb()
    shape_game["font"] = font.Font(size=30)
    shape_game["entry"] = Entry(root)
    shape_game["entry"].pack(side=BOTTOM, fill=X)
    shape_game["start_button"] = Button(
        root, text="Start Game", highlightbackground="#b4ff8b", command=next_shape
    )
    shape_game["start_button"]["font"] = shape_game["font"]
    shape_game["start_button"].pack(side=BOTTOM, fill=X)
    root.mainloop()


if __name__ == "__main__":
    driver()
