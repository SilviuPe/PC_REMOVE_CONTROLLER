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

        self.last_mouse_pos = []
        self.last_press = None
        self.last_button = None

        self.previous_data = {
            'left' :{
                'pressed' : False,
                'position' : []
            },
        }

        self.keys_hold = {
            'key_still_pressed' : False,
            'keys_hold' : []
        }


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

            if data['button'].split('.')[1] == 'left':

                self.previous_data['left']['pressed'] = True
                self.previous_data['left']['position'] = [x_value_from_percent, y_value_from_percent]


            print("Mouse down", data['button'].split('.')[1])
            pyautogui.mouseDown(button=data['button'].split('.')[1], x=x_value_from_percent, y=y_value_from_percent)

        else:

            if data['button'].split('.')[1] == 'left':

                self.previous_data['left']['pressed'] = False

                if self.previous_data['left']['position'][0] != x_value_from_percent or self.previous_data['left']['position'][1] != y_value_from_percent:
                        print("Dragging detected!")
                        pyautogui.mouseDown(button=data['button'].split('.')[1], x=self.previous_data['left']['position'][0], y=self.previous_data['left']['position'][1])
                        time.sleep(0.25)
                        pyautogui.moveTo(x_value_from_percent, y_value_from_percent, duration=0.25)
                        time.sleep(0.25)
                        pyautogui.mouseUp(button=data['button'].split('.')[1]) # , x=x_value_from_percent, y=y_value_from_percent
                        self.previous_data['left']['position'] = [x_value_from_percent,y_value_from_percent]
                        return

            print("Mouse up", data['button'].split('.')[1])
            pyautogui.mouseUp(button=data['button'].split('.')[1], x=x_value_from_percent, y=y_value_from_percent)

    def key_input(self,data) -> None:

        if 'type' in data:

            type_ = data['type']
            if len(data['key_char']) > 1:

                key = data['key_char'].split('.')[1]
            else:
                key = data['key_char']
            if type_ == 'press':
                pyautogui.keyDown(key)

            elif type_ == 'release':
                pyautogui.keyUp(key)

    def scroll(self, data):

        if 'dy' in data and 'dx' in data:

            direction_y = data['dy']
            direction_x = data['dx']
            position = (data['x'],data['y'])
            print(position)
            try:
                if direction_y != 0:
                    pyautogui.moveTo(x=position[0], y=position[1])
                    pyautogui.scroll(clicks= direction_y*120, x=position[0], y=position[1])

                if direction_x != 0:
                    pyautogui.moveTo(x=position[0], y=position[1])
                    pyautogui.keyDown('shift')
                    pyautogui.scroll(clicks=direction_x * 120, x=position[0], y=position[1])
                    pyautogui.keyUp('shift')

            except Exception as error:

                print("Error trying to scroll", str(error))







