from typing import List

from .queue import Queue


class RabbitMQ(Queue):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def send_messages(self, queue: str, messages: List[str]):
        pass

    def receive_message(self, queue: str):
        pass
