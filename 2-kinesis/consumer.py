import boto3
import time
import json
import os

client = boto3.client('kinesis', 'us-east-1')

streamName = "TestStream"
streamInfo = client.describe_stream(StreamName=streamName)
shardId = streamInfo['StreamDescription']['Shards'][0]['ShardId']

shardIterator = client.get_shard_iterator(StreamName=streamName, ShardId=shardId, ShardIteratorType='LATEST')['ShardIterator']

while shardIterator is not None:
  retrievedData = client.get_records(ShardIterator=shardIterator, Limit=1)
  shardIterator = retrievedData['NextShardIterator']
  if len(retrievedData['Records']) > 0:
    msg = json.loads(retrievedData['Records'][0]['Data'].decode('utf-8'))
    os.system('clear')
    print(msg['message'], end=" ")
  time.sleep(1)


    
