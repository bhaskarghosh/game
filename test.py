from threading import Thread
import threading


def raw_input_with_timeout(prompt, timeout=2):
    print(prompt)
    timer = threading.Timer(timeout, Thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return astring


raw_input_with_timeout("Hello", 2)

