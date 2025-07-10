import sockets
import json

from threading import Thread


class Server(object):

    def __init__(self) -> None:


        # sockets.gethostbyname -> localhost
        self.address = sockets.gethostbyname()
        self.port = 44324

        # create the server socket
        self.server_socket = self.create_server((self.address, self.port))

        # clients connected to the server
        self.clients = list()

        # start the listener for new clients
        Thread(target=self.listen_for_clients).start()


    def create_server(self, binder_data : tuple) -> sockets.socket | None:
        """
        Method to create a server
        :binder_data: tuple -> (address, port)
        :return:  socket object
        """
        try:
            socket = sockets.socket(sockets.AF_INET, sockets.SOCK_STREAM)
            socket.bind(binder_data)

            socket.listen()

            return socket

        except Exception as error:

            print(str(error))
            return None


    def listen_for_clients(self) -> None:
        """
        Method to listen to clients
        :return:
        """

        while True:

            # accept client

            client_socket, client_address = self.server_socket.accept()

            client_data = {
                'socket' : client_socket,
                'address' : client_address,
            }
            self.clients.append(client_data)

    def remove_client(self) -> None:
        """
        Method to remove a client
        :return:
        """

        pass

    def send_data_to_all_clients(self, data : dict) -> None:
        """
        Method to send data to all clients

        :param: data -> dictionary containing the action and value
                eg.
                { "move" :
                    { "x" : 200,
                      "y" : 400
                    }
                }

        :return: None
        """

        try:

            serialized_data = json.dumps(data).encode()

            for client in self.clients:

                client['socket'].sendall(serialized_data)

        except Exception as error:

            print(str(error))