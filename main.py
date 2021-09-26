from argparse import ArgumentParser

from entities.user import User
from generator.user_generator import UserGenerator
from producer.user_producer import UserProducer

def parse_command_line_args():
    arg_parser  = ArgumentParser()

    arg_parser.add_argument("--topic", required=False, default='camp-users2', help='Topic name')
    arg_parser.add_argument("-bootstrap-servers", required=False, default='localhost:9092',
                            help='Bootstrap server address')
    arg_parser.add_argument('--schema-registry', required=False, default='http://localhost:8081',
                            help='Schema registry url')
    arg_parser.add_argument('--schema-file', required=False, default='create-user-request.avsc',
                            help='file name of Avro schema to use')
    return arg_parser.parse_args()

if __name__ == '__main__':
    args = parse_command_line_args()
    user_producer = UserProducer(args)
    user = User.generate_random_user()
    for users in UserGenerator.generate():
        user_producer.send_records(users)


# to check: ./bin/kafka-avro-console-consumer --topic user-test --bootstrap-server localhost:9092 --from beginning
