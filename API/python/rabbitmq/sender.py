
import common

CreateConnection = common.CreateConnection
OpenQueue = common.OpenQueue


def SendOnQueue(queue_name, message):
    common.rabbitmq_connection.basic_publish(
        exchange='', routing_key=queue_name, body=message)


if __name__ == '__main__':
    CreateConnection(port=5673, username='tmri4', password='tmri4', virtual_host='tmri4', host='localhost')
    OpenQueue('test_python')
    for i in range(7):
        SendOnQueue('test_python', 'Python Test Message {0}'.format(i))