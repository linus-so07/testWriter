import keyboard as kbd
import time
import random
import sys

string = """The purpose of this project is to design and examine a simple electric motor in order to deepen the understanding of the principles of electromagnetism and its practical applications. The work aims to demonstrate how electrical energy can be converted into mechanical motion and to identify the factors that influence the motor’s efficiency and performance. By building the motor in practice, the project also seeks to highlight the connection between theory and construction. Furthermore, electric motors play an important role in the transition toward more environmentally friendly energy solutions, as they can help reduce emissions compared to combustion engines.

"""

adjacent_keys = {
    'a': 'qwsz',
    'b': 'vghn',
    'c': 'xdfv',
    'd': 'ersfcx',
    'e': 'wsdr',
    'f': 'rtgvcd',
    'g': 'tyhbvf',
    'h': 'yujnbg',
    'i': 'ujko',
    'j': 'uikmnh',
    'k': 'iolmj',
    'l': 'opk',
    'm': 'njk',
    'n': 'bhjm',
    'o': 'iklp',
    'p': 'ol',
    'q': 'wa',
    'r': 'edft',
    's': 'wedxza',
    't': 'rfgy',
    'u': 'yhji',
    'v': 'cfgb',
    'w': 'qesa',
    'x': 'zsdc',
    'y': 'tghu',
    'z': 'asx',
}

paused = False
Run = True


def check_killswitch():
    if kbd.is_pressed("ctrl+0"):
        print("Exiting Program")
        sys.exit(0)


def random_adjacent_key(char):
    if char.lower() in adjacent_keys:
        neighbors = adjacent_keys[char.lower()]
        wrong = random.choice(neighbors)
        return wrong.upper() if char.isupper() else wrong
    return char


def pause_game():
    global paused
    paused = not paused
    

kbd.add_hotkey("ctrl+2", pause_game)

time.sleep(5)


for char in string:
    check_killswitch()
    while paused:
        time.sleep(0.1)
    if random.random() < 0.02 and char.isalpha():
        typo = random_adjacent_key(char)
        kbd.write(typo)
        time.sleep(random.uniform(0.05, 0.2))
        kbd.press_and_release('backspace')
        time.sleep(random.uniform(0.05, 0.3))
    kbd.write(char)
    time.sleep(random.uniform(0.05, 0.25))
    if char in ",;:":
        time.sleep(random.uniform(0.3, 0.6))
    elif char in ".!?":
        time.sleep(random.uniform(0.6, 1.2))
    elif char == "\n":
        time.sleep(random.uniform(0.5, 1.0))
