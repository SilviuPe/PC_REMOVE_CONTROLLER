from connection import Server
from monitor import Monitor
from threading import Thread
from time import sleep


"""
Actions and key/values:

{
    "action" : "move" | "click" | "scroll" | "pressed",
    "data" : .......
}


    DATA:
    
        "move" : { "position" : { "x" : int value, "y" : int value } }
        "click" : { "pressed" : boolean, "released" : boolean} -> both cannot be true
        "scroll" : { "position" : { "x" : int value, "y" : int value }}
        "pressed" : { "key_char" : string | None, "key" : string | None, "pressed" : boolean, "released" }
"""


class MainApp(object):

    """
    Object to combine and manage the monitor with the server ( main app )
    """

    def __init__(self) -> None:

        # Monitor object
        self.server = None
        self.monitor = None

        self.mouse_thread = None
        self.keyboard_thread = None


    def start_server(self) -> None:
        self.server = Server()
        self.monitor = Monitor(self.handle_event)

        self.mouse_thread = Thread(target=self.monitor.start_mouse_listener)
        self.keyboard_thread = Thread(target=self.monitor.start_keyboard_listener)

        self.mouse_thread.start()
        self.keyboard_thread.start()

    def handle_event(self, event : dict) -> None:
        """
        Method to get the event data and values
        :param event: dict with the event type and data
        :return: None
        """
        self.server.send_data_to_all_clients(event)
        # pass
        # print(event)


MainApp()