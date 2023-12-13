import sys
import time

def print_string_anim(string, seconds):
    print("Printing: ", end="")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(seconds / len(string))

    print("\nPrinting complete!")

def simulate_loading(seconds):
    print("Loading: ", end="")
    for i in range(1, 21):
        sys.stdout.write(f"▊")
        sys.stdout.flush()
        time.sleep(seconds / 20)

    print("\nLoading complete!")
