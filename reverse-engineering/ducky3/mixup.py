import random

data = """ "0": "00,00,27",
    "1": "00,00,1e",
    "2": "00,00,1f",
    "3": "00,00,20",
    "4": "00,00,21",
    "5": "00,00,22",
    "6": "00,00,23",
    "7": "00,00,24",
    "8": "00,00,25",
    "9": "00,00,26",
    "CTRL": "01,00,00",
    "CONTROL": "01,00,00",
    "SHIFT": "02,00,00",
    "ALT": "04,00,00",
    "GUI": "08,00,00",
    "WINDOWS": "08,00,00",
    "COMMAND": "08,00,00",
    "a": "00,00,04",
    "A": "02,00,04",
    "b": "00,00,05",
    "B": "02,00,05",
    "c": "00,00,06",
    "C": "02,00,06",
    "d": "00,00,07",
    "D": "02,00,07",
    "e": "00,00,08",
    "E": "02,00,08",
    "f": "00,00,09",
    "F": "02,00,09",
    "g": "00,00,0a",
    "G": "02,00,0a",
    "h": "00,00,0b",
    "H": "02,00,0b",
    "i": "00,00,0c",
    "I": "02,00,0c",
    "j": "00,00,0d",
    "J": "02,00,0d",
    "k": "00,00,0e",
    "K": "02,00,0e",
    "l": "00,00,0f",
    "L": "02,00,0f",
    "m": "00,00,10",
    "M": "02,00,10",
    "n": "00,00,11",
    "N": "02,00,11",
    "o": "00,00,12",
    "O": "02,00,12",
    "p": "00,00,13",
    "P": "02,00,13",
    "q": "00,00,14",
    "Q": "02,00,14",
    "r": "00,00,15",
    "R": "02,00,15",
    "s": "00,00,16",
    "S": "02,00,16",
    "t": "00,00,17",
    "T": "02,00,17",
    "u": "00,00,18",
    "U": "02,00,18",
    "v": "00,00,19",
    "V": "02,00,19",
    "w": "00,00,1a",
    "W": "02,00,1a",
    "x": "00,00,1b",
    "X": "02,00,1b",
    "y": "00,00,1c",
    "Y": "02,00,1c",
    "z": "00,00,1d",
    "Z": "02,00,1d",
    "!": "02,00,1e",
    "@": "02,00,1f",
    "#": "02,00,20",
    "$": "02,00,21",
    "%": "02,00,22",
    "^": "02,00,23",
    "&": "02,00,24",
    "*": "02,00,25",
    "(": "02,00,26",
    ")": "02,00,27",
    "ENTER": "00,00,28",
    "ESC": "00,00,29",
    "ESCAPE": "00,00,29",
    "BACKSPACE": "00,00,2a",
    "TAB": "00,00,2b",
    "SPACE": "00,00,2c",
    " ": "00,00,2c",
    "-": "00,00,2d",
    "_": "02,00,2d",
    "=": "00,00,2e",
    "+": "02,00,2e",
    "[": "00,00,2f",
    "{": "02,00,2f",
    "]": "00,00,30",
    "}": "02,00,30",
    "\\": "00,00,31",
    "|": "02,00,31",
    ";": "00,00,33",
    ":": "02,00,33",
    "'": "00,00,34",
    "\"": "02,00,34",
    "`": "00,00,35",
    "~": "02,00,35",
    ",": "00,00,36",
    "<": "02,00,36",
    ".": "00,00,37",
    ">": "02,00,37",
    "/": "00,00,38",
    "?": "02,00,38",
    "CAPSLOCK": "00,00,39",
    "F1": "00,00,3a",
    "F2": "00,00,3b",
    "F3": "00,00,3c",
    "F4": "00,00,3d",
    "F5": "00,00,3e",
    "F6": "00,00,3f",
    "F7": "00,00,40",
    "F8": "00,00,41",
    "F9": "00,00,42",
    "F10": "00,00,43",
    "F11": "00,00,44",
    "F12": "00,00,45",
    "PRINTSCREEN": "00,00,46",
    "SCROLLLOCK": "00,00,47",
    "PAUSE": "00,00,48",
    "BREAK": "00,00,48",
    "INSERT": "00,00,49",
    "HOME": "00,00,4a",
    "PAGEUP": "00,00,4b",
    "DELETE": "00,00,4c",
    "DEL": "00,00,4c",
    "END": "00,00,4d",
    "PAGEDOWN": "00,00,4e",
    "RIGHTARROW": "00,00,4f",
    "RIGHT": "00,00,4f",
    "LEFTARROW": "00,00,50",
    "LEFT": "00,00,50",
    "DOWNARROW": "00,00,51",
    "DOWN": "00,00,51",
    "UPARROW": "00,00,52",
    "UP": "00,00,52",
    "NUMLOCK": "00,00,53",
    "MENU": "00,00,65",
    "APP": "00,00,65" """

lines = data.split("\n")

keys = []
values = []
for line in lines:
    #print(line)
    KEY = line.split(":")[0].strip()
    VALUE = line.split(":")[1].strip()
    keys.append(KEY)
    values.append(VALUE)

# mixup
random.shuffle(values)
for i in range(len(keys)):
    print(keys[i]+": "+values[i])