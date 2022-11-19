import base64
import json
import os
from google.cloud import pubsub_v1

publisher= pubsub_v1.PublisherClient()
PROJECT_ID=os.getenv('new-neo-368606')

def readings(request):
    data =request.data

    if data is None:
        print('request.data is empty')
        return('request.data is empty',400)

    print(f'request data:{data}')

    data_json=json.loads(data)
    print(f'request data json:{data_json}')

    productName=data_json['productName']
    categoria =data_json['categoria']
    precio =data_json['precio']
    print(f'Nombre del producto:{productName}')
    print(f'Categoria del producto:{categoria}')
    print(f'Precio del producto:{precio}')
    
    topic_path='projects/new-neo-368606/topics/arquitectura-pub-sub'
    message_json=json.dumps({
        'data':{'message':'Data de un nuevo producto!'},
        'readings':{
            'productName':productName,
            'categoria':categoria,
            'precio':precio
        }
    })

    message_bytes=message_json.encode('utf-8')

    try:
        publish_future=publisher.publish(topic_path,data=message_bytes)
        publish_future.result()
    except Exception as e:
        print(e)
        return (e,500)
        
    return ('Message received and published to pubsub',200)