from connection import Client
from inputs_control import InputsController





class MainApp(object):

    def __init__(self) -> None:

        self.client =  None
        self.controller = None


    def start_client(self) -> None:
        self.client = Client(self.handle_data)
        self.controller = InputsController()
        self.client.receive_data()


    def handle_data(self, data: dict) -> None:

        if 'type' in data:
            type_ = data['type']
            print(data)
            if type_ == "move":

                self.controller.move(data['data']['position'])

            elif type_ == "click":

                self.controller.click(data['data'])

            elif type_ == "release" or type_ == "press":

                self.controller.key_input(data)

            elif type_ == "mouse_scroll":

                self.controller.scroll(data)