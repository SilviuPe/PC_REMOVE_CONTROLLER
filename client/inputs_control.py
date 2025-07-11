import pyautogui
import time

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# Wait 3 seconds so you can switch to the target window

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

class InputsController(object):

    """
    Object to control the mouse actions
    """

    def __init__(self) -> None:

        pass

    def move(self, data : dict) -> None:
        """

        :param data -> dict
        :return: None
        """

        x_value_from_percent = SCREEN_WIDTH * data['x'] / 100
        y_value_from_percent = SCREEN_HEIGHT * data['y'] / 100

        pyautogui.moveTo(x_value_from_percent, y_value_from_percent, duration=0.01)

    def click(self, data : dict) -> None:
        """
        Method used to press left click
        :param: data -> dict
        :return: None
        """
        print(data, "test")
        position = data['position']
        print(position)

        x_value_from_percent = SCREEN_WIDTH * position['x'] / 100
        y_value_from_percent = SCREEN_HEIGHT * position['y'] / 100

        if data['pressed']:
            print("Mouse down", data['button'].split('.')[1])
            pyautogui.mouseDown(button=data['button'].split('.')[1], x=x_value_from_percent, y=y_value_from_percent)

        else:
            print("Mouse up", data['button'].split('.')[1])
            pyautogui.mouseUp(button=data['button'].split('.')[1], x=x_value_from_percent, y=y_value_from_percent)



