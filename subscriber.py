import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError

credentials_path='/home/ander/Ulima/pubsub/new-neo-368606-60d4abe8acbd.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

timeout=5.0

subscriber = pubsub_v1.SubscriberClient()
subscription_path='projects/new-neo-368606/subscriptions/arquitectura-pub-sub-sub'

def callback(message):
    print(f'Received message:{message}')
    print(f'Data:{message.data}') 
    if message.attributes:
        print(f'Attributes:')
        for key in message.attributes:
            value=message.attributes.get(key)
            print(f'{key}:{value}')
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f'Listening for messages on {subscription_path}...')

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()

