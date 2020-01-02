from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(100000):
    data = {'producer B - number' : e}
    producer.send('KafkaTask', value=data)
    sleep(2)