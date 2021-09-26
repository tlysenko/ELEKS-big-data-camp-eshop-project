import json

from producer.base_producer import BaseProducer


class UserProducer(BaseProducer):

    def __int__(self, args):
        super().__init__(args)

    def send_record(self, key: str, value: json):
        try:
            self.producer.produce(topic=self.topic, key=key, value=value)
        except Exception as e:
            print(f'Exception while producing record value - {value} to topic - {self.topic}:{e}')
        else:
            print(f'Succsesfully producing record value - {value} to topic - {self.topic}')

    def send_records(self, users: list):
        for user in users:
            self.send_record(key=user.email, value=user.to_json())
        self.producer.flush()
