import os
import boto3
from typing import List
from dotenv import load_dotenv

from .queue import Queue

load_dotenv()


class SQS(Queue):
    def __init__(self, host: str, port: int, queue: str):
        self.host = host
        self.port = port
        self.queue = queue
        self.region_name = os.getenv('AWS_REGION')
        self.account_number = os.getenv('ACCOUNT_NUMBER')

        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

        queue = boto3.client('sqs', region_name=self.region_name,
                             aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key)

    def send_messages(self, queue: str, messages: List[str]):
        self.queue_url = f"https://sqs.{self.region_name}.amazonaws.com/{self.account_number}/{self.queue}"
        pass

    def receive_message(self, queue: str):
        pass
