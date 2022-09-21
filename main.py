from dotenv import load_dotenv
from pynput.keyboard import Key, Listener
import pyperclip

from source.essay import essay
from source.expand import expand
from source.paraphrase import paraphrase
from source.keypoints import keypoints
from source.qa import qa

HOTKEYS = {essay: (['Key.cmd'] * 3),
          qa: ['Key.cmd'] * 2,
          paraphrase: ['Key.cmd'],
          keypoints: ['Key.alt'] * 2,
          expand: ['Key.alt']}

TRIGGERS = [["'c'", "Key.cmd"], ["'x'", "Key.cmd"]]




load_dotenv()
hist = [None] * 10
HOTKEYS = dict(sorted(HOTKEYS.items(), key=lambda x: len(x[1]), reverse=True))
TRIGGERS = sorted(TRIGGERS, key=lambda x: len(x), reverse=True)
def on_press(key):
    global hist
    hist.insert(0, str(key))
    hist = hist[:-1]
    trigger = triggered(hist)
    if trigger:
        text = pyperclip.paste()
        l = len(trigger)
        for func, keys in HOTKEYS.items():
            if hist[l:l+len(keys)] == keys:
                print(func)
                pyperclip.copy("")
                pyperclip.copy(func(text)['result'])
                break            

def on_release(key):
    return

def triggered(hist):
    for keys in TRIGGERS:
        if hist[0:len(keys)] == keys:
            return keys


with Listener(on_press=on_press, on_release=on_release) as listener:
    print("started")
    listener.join()