import socket
import json

class Client(object):

    """
    Object to connect to the server and receive data
    """

    def __init__(self, callback) -> None:


        # sockets.gethostbyname -> localhost
        self.address = socket.gethostbyname('192.168.0.108')
        self.port = 44324

        # create the server socket
        self.client_socket = None
        self.create_client((self.address, self.port))

        self.callback = callback


    def create_client(self, connection_data: tuple) -> None:
        """
        Method to create a client
        :connection_data: tuple -> (address, port)
        :return:  socket object
        """
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(connection_data)

        except Exception as error:

            print(str(error))


    def receive_data(self) -> None:

        while True:

            try:

                data = self.client_socket.recv(1024).decode()
                data = data.split('\n')
                print(data)

                if not data:

                    break

                else:

                    for action in data:

                        serialized_action = json.loads(action)
                        print(serialized_action)
                        self.callback(serialized_action)
                    print("Received data:", data)


            except Exception as error:

                print("Error occurred while tried to receive data", str(error))