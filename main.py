import keyboard
import keyboard as kbd
import time
import random
import sys

string = """"""


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


def random_adjacent_key(char):
    if char.lower() in adjacent_keys:
        neighbors = adjacent_keys[char.lower()]
        wrong = random.choice(neighbors)
        return wrong.upper() if char.isupper() else wrong
    return char


run = True
time.sleep(5)

while run:
    for char in string:
        
        if keyboard.is_pressed("Esc"):
            sys.exit(0)
        
        if random.random() < 0.02 and char.isalpha():
            typo = random_adjacent_key(char)
            kbd.write(typo)
            time.sleep(random.uniform(0.05, 0.2))
            kbd.press_and_release('backspace')
            time.sleep(random.uniform(0.05, 0.3))
        kbd.write(char)
        time.sleep(random.uniform(0.1, 0.3))
        if char in ",;:":
            time.sleep(random.uniform(0.3, 0.6))
        elif char in ".!?":
            time.sleep(random.uniform(0.6, 1.2))
        elif char == "\n":
            time.sleep(random.uniform(0.5, 1.0))

    break
    