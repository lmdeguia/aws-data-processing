import boto3
import time
from Stream import Stream

client = boto3.client('kinesis', 'us-east-1')
streamName = "TestStream"
stream = Stream(client)
stream.name = streamName

def formatAndInsertRecord(stream, message):
  data = {
    'message': message
  }
  response = stream.put_record(data, 'key')
  return response

s = "Dora! Boots! Come on, Dora! Do-do-do-d-Dora alright! Do-do-do-d-Dora Do-do-do-d-Dora Do-do-do-d-Dora let's go! Dora, Dora, Dora the explorer Dora! Boots and super cool exploradora Need your help grab your backpack Let's go, jump in ¡vámonos! You can lead the way, hey, hey Do-d-Dora, do-d-Dora Do-d-Dora, do-d-Dora Swiper, no swiping! Swiper, no swiping! Oh, man Dora the explorer!".split(" ")

if __name__ == '__main__':
  idx = 0
  n = len(s)
  while True:
    if idx == n: idx = 0
    response = formatAndInsertRecord(stream, s[idx])
    print(response)
    idx += 1
    time.sleep(5)
    




