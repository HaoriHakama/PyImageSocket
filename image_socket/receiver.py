import socketserver
import base64
from queue import Queue


class ImageReceiverHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        image_data_size = int.from_bytes(self.request.recv(4), byteorder="big")
        image_data = self.receive_data(image_data_size)
        image_data = base64.b64decode(image_data)

        text_size = int.from_bytes(self.request.recv(4), byteorder="big")
        text = self.receive_data(text_size).decode()

        self.server.received_data_q.put([image_data, text])

    def receive_data(self, size):
        data = b""
        while len(data) < size:
            more_data = self.request.recv(size - len(data))
            if not more_data:
                raise Exception("Fail to receive all data")
            data += more_data
        return data


class Receiver(socketserver.TCPServer):
    def __init__(
        self, server_address, RequestHandlerClass, bind_and_activate=True
    ):
        super().__init__(
            server_address, RequestHandlerClass, bind_and_activate
        )
        self.received_data_q = Queue()
