import socket
import json

class Client(object):

    """
    Object to connect to the server and receive data
    """

    def __init__(self, callback) -> None:

        self.running = True

        # sockets.gethostbyname -> localhost
        self.address = socket.gethostbyname('192.168.0.100') # Same as the server
        self.port = 4500 # Same as the server

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

    def close(self) -> None:
        self.client_socket.close()
        self.running = False


    def receive_data(self) -> None:

        while self.running:

            try:

                data = self.client_socket.recv(8192).decode()
                data = data.split('\n')

                if not data:

                    break

                else:

                    for action in data:

                        try:
                            serialized_action = json.loads(action)
                            self.callback(serialized_action)
                        except Exception as error:

                            continue


            except Exception as error:

                print("Error occurred while tried to receive data", str(error))