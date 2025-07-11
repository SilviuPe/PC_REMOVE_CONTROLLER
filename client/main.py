from connection import Client
from inputs_control import InputsController





class MainApp(object):

    def __init__(self) -> None:

        self.client = Client(self.handle_data)
        self.controller = InputsController()
        self.client.receive_data()

    def handle_data(self, data: dict) -> None:

        if 'type' in data:
            print(data['data']['position'])
            type_ = data['type']

            if type_ == "move":

                self.controller.move(data['data']['position'])

            elif type_ == "click":

                self.controller.click(data['data'])

MainApp()