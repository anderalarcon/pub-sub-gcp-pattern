import os
from google.cloud import pubsub_v1

credentials_path='/home/ander/Ulima/pubsub/new-neo-368606-60d4abe8acbd.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher= pubsub_v1.PublisherClient()
topic_path='projects/new-neo-368606/topics/arquitectura-pub-sub'

data='Enviar mensaje desde Publisher'
data=data.encode('utf-8')
attributes = {
    'notification': 'True',
    'message': 'Nuevo producto disponible',
    'asunto':'Oferta'
}
future=publisher.publish(topic_path,data, **attributes)
print(f'published message id {future.result()}')