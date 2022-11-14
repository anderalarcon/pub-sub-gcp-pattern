import requests
import json

def send_message_to_google_cloud():
    url='https://us-central1-new-neo-368606.cloudfunctions.net/readings'
    data={
        'sensorName':'sensor1',
        'temperature':20,
        'humidity':30
    }
    headers={'Content-type':'application/json','Accept':'text/plain'}
    r=requests.post(url,data=json.dumps(data),headers=headers)
    print(f'r={r}')
if __name__ == '__main__':
    send_message_to_google_cloud()