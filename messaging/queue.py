from abc import ABC, abstractmethod
from typing import List


class Queue(ABC):
    @abstractmethod
    def send_messages(self, queue: str, messages: List[int]):
        pass

    @abstractmethod
    def receive_message(self, queue: str):
        pass
