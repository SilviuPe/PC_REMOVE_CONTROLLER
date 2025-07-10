import threading
from pynput import mouse, keyboard


def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    if pressed:
        print(f"{button} pressed at ({x}, {y})")
    else:
        print(f"{button} released at ({x}, {y})")

def on_scroll(x, y, dx, dy):
    print(f"Scrolled {'down' if dy < 0 else 'up'} at ({x}, {y})")

def on_press(key):
    try:
        print(f"Key {key.char} pressed")
    except AttributeError:
        print(f"Special key {key} pressed")

def on_release(key):
    print(f"Key {key} released")
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def start_mouse_listener():
    with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
        listener.join()

def start_keyboard_listener():
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

# Define handlers (reuse from above or customize)

# Start both listeners
threading.Thread(target=start_mouse_listener).start()
threading.Thread(target=start_keyboard_listener).start()
