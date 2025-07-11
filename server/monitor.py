import pyautogui
import math

from pynput import mouse, keyboard
from typing import Any


SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
"""
Actions and key/values:

{
    "action" : "move" | "click" | "scroll" | "pressed" | "released",
    "data" : .......
}


    DATA:

        "move" : { "position" : 
                    { 
                        "x" : int value, 
                        "y" : int value 
                    } 
                }
        
        "click" : { 
                    "position" : 
                                { 
                                    "x" : int value, 
                                    "y" : int value 
                                },
                    "pressed" : "release" | "pressed",
                    "button" : "left click, right click, and so on..."}
        
        "scroll" : { 
            "data" : {
                "position" : 
                    { 
                        "x" : int value, 
                        "y" : int value,
                        "dx" : int value,
                        "dy" : int value
                    },
            }}
            
            
            
        "pressed" : 
            { "key_char" : string | None }
            
            
        "release" : 
            { "key_char" : string | None }
"""


class Monitor(object):

    def __init__(self, callback: Any):
        self.callback = callback


    def on_move(self, x, y):

        percent_of_screen_x = 100 * x / SCREEN_WIDTH
        percent_of_screen_x = math.trunc(percent_of_screen_x * 100) / 100

        percent_of_screen_y = 100 * y / SCREEN_HEIGHT
        percent_of_screen_y = math.trunc(percent_of_screen_y * 100) / 100

        event_data = {"type": "move", "data" : {
            "position" : {
                "x": percent_of_screen_x, "y": percent_of_screen_y
            }
        }}

        self.callback(event_data)

    def on_click(self, x, y, button, pressed):
        event_data = {
            "type": "click",
            "data" : {
                "position" : {
                    "x": x,
                    "y": y,
                },
                "button": str(button),
                "pressed": pressed
            }
        }
        print(str(button))

        self.callback(event_data)

    def on_scroll(self, x, y, dx, dy):
        event_data = {
            "type": "mouse_scroll",
            "x": x,
            "y": y,
            "dx": dx,
            "dy": dy
        }
        self.callback(event_data)

    def on_press(self, key):
        try:
            key_val = key.char
        except AttributeError:
            key_val = str(key)

        event_data = {
            "type": "press",
            "key_char": key_val
        }
        self.callback(event_data)

    def on_release(self, key):
        event_data = {
            "type": "release",
            "key_char": str(key)
        }
        self.callback(event_data)

        # if key == keyboard.Key.esc:
        #     # Stop the listener
        #     return False

    def start_mouse_listener(self):
        with mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll) as listener:
            listener.join()

    def start_keyboard_listener(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
            listener.join()
