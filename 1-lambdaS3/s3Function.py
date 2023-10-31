import boto3
import os

def s3Put(srcFile, dstFile):
  s3 = boto3.client('s3')
  s3.upload_file(srcFile, os.environ['BucketName'], dstFile)

def s3Get():
  s3 = boto3.client('s3')
  bucket='s3lambda-lmdeguia'
  data = s3.get_object(Bucket=bucket, Key='readme.txt')
  contents = data['Body'].read()
  print(contents)
  return contents

def lambda_handler(event, context):
  fileName = 'test.txt'
  s3Put(fileName, fileName)
  contents = s3Get()
  return contents