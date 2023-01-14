from pynput import keyboard
import time
import os


class Timer:
    def __init__(self):
        self.starttime = time.time()

    def interval(self):
        now = time.time()
        interval = now - self.starttime
        self.starttime = now
        return interval


def on_press(key):
    keystr = str(key).lower()
    if keystr in timers:
        return
    timers[keystr] = Timer()
    print(f"--gap {inter.interval()*1000 :.2f}ms")
    print(f"Key Down: {key}")


def on_release(key):
    print(f"--gap {inter.interval()*1000 :.2f}ms")
    keystr = str(key).lower()
    print(f"Key Up: {key} after {timers.pop(keystr).interval()*1000:.2f}ms")
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key == keyboard.Key.backspace:
        os.system("clear")
        print("Press ESC to exit")


if __name__ == "__main__":
    print("Keyboard listener started, press ESC to exit")
    inter = Timer()
    timers = {}
    with keyboard.Listener(
        on_press=on_press, on_release=on_release, suppress=True
    ) as listener:
        listener.join()
