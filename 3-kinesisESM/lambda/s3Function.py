import json
import base64
import boto3

client = boto3.client('s3')
name='s3lambda-lmdeguia'
key = 'read.txt'

def lambda_handler(event, context):
    obj = client.get_object(Bucket=name, Key=key)
    objBody = obj.get('Body').read().decode('utf-8') + " "
    
    try:
        data64 = event['Records'][0]['kinesis']['data']
        data = json.loads(base64.b64decode(data64).decode('utf-8'))
        msg = data["message"]
        objBody += msg
        print(f'msg={msg} objBody={objBody}')
        client.put_object(Body=objBody, Bucket=name, Key=key)
    except:
        print("")
