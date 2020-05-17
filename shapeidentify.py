#!/usr/local/bin/python3

import ast
import random
import time, threading
from threading import Thread
import sys, select

shape_game = {}
answer = ""

"""
https://stackoverflow.com/questions/25029537/interrupt-function-execution-from-another-function-in-python

"""


class InterruptExecution(Exception):
    pass


def get_answer():
    ans = "Nothing"
    print("Please provide input in 2 seconds! (Hit Ctrl-C to start)")
    try:
        time.sleep(2)  # could use a backward counter to be preeety :)
        print("No input is given.")
    except KeyboardInterrupt:
        ans = eval(input("Input x:"))
        print("You, you! You know something.")
    return ans


def game_loop():
    shape_game["completed"] = True


def try_loop():
    shape_game["try"] = True
    raise InterruptExecution("Move on")


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


def driver():
    default_level = 1
    shape_game["completed"] = False

    user_suffix = str(random.randrange(0, 101, 2))
    shape_game["user"] = "user" + user_suffix
    load_shapesdb()
    load_guide()
    load_level_shape_info()
    how_many = int(shape_game["level_shape"][default_level])
    t_level = 60 / how_many
    print(t_level)

    print(shape_game)
    start_time = time.perf_counter()
    end_time = start_time + 6
    print(start_time)
    print(end_time)
    threading.Timer(3, game_loop).start()
    while not (shape_game["completed"]):
        shape_game["try"] = False
        i = 0
        # threading.Timer(1, try_loop).start()
        while i < how_many:
            i = i + 1
            print(i)
            print(next_shape())
            k, o, e = select.select([sys.stdin], [], [], t_level)

            if k:
                print("You said", sys.stdin.readline().strip())
            else:
                print("You said nothing!")
            # time.sleep(2)
            print("completed a try")
        time_left = end_time - time.perf_counter()
        if time_left >= 0:
            time.sleep(time_left)
        print("completed all")
    print("Want to play another Game?")


if __name__ == "__main__":
    driver()
