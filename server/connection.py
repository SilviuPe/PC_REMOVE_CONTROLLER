import socket
import json

from threading import Thread


class Server(object):

    def __init__(self) -> None:


        # sockets.gethostbyname -> localhost
        self.address = socket.gethostbyname('192.168.0.108')
        self.port = 44324

        # create the server socket
        self.server_socket = None
        self.create_server((self.address, self.port))

        # clients connected to the server
        self.clients = list()

        # start the listener for new clients
        Thread(target=self.listen_for_clients).start()


    def create_server(self, binder_data : tuple) -> None:
        """
        Method to create a server
        :binder_data: tuple -> (address, port)
        :return:  socket object
        """
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind(binder_data)

            self.server_socket.listen()

        except Exception as error:

            print(str(error))



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

            print("New client has connected: ", client_data['address'])

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
        :return: None
        """

        try:

            serialized_data = (json.dumps(data) + "\n").encode()

            for client in self.clients:

                try:
                    client['socket'].send(serialized_data)


                    print(f"Successfully sent data to {client['address'][0]}")
                except Exception as error:

                    print(f"Error trying to sent data to {client['address'][0]}",str(error))

                    client['socket'].close()
                    self.clients.remove(client)

        except Exception as error:

            print(str(error))