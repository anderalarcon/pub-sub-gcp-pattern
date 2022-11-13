import os
from google.cloud import pubsub_v1

credentials_path='/home/ander/Ulima/pubsub/galvanic-flame-368521-31e6c9c62cb4.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher= pubsub_v1.PublisherClient()
topic_path='projects/galvanic-flame-368521/topics/pubsubpattern'

data='READY'
data=data.encode('utf-8')
attributes = {
    'notification': 'True',
    'message': 'Nuevo producto disponible',
    'asunto':'Oferta'
}
future=publisher.publish(topic_path,data, **attributes)
print(f'published message id {future.result()}')