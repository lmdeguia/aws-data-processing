from logger import logger
import json

class Stream:

  def __init__(self, kinesis_client):
        """
        :param kinesis_client: A Boto3 Kinesis client.
        """
        self.kinesis_client = kinesis_client
        self.name = None
        self.details = None
        self.stream_exists_waiter = kinesis_client.get_waiter("stream_exists")

  def create(self, name, wait_until_exists=True):
    try:
        self.kinesis_client.create_stream(StreamName=name, ShardCount=1)
        self.name = name
        logger.info("Created stream %s.", name)
        if wait_until_exists:
            logger.info("Waiting until exists.")
            self.stream_exists_waiter.wait(StreamName=name)
            self.describe(name)
    except:
        logger.exception("Couldn't create stream %s.", name)
        raise

  def delete(self):
    """
    Deletes a stream.
    """
    try:
        self.kinesis_client.delete_stream(StreamName=self.name)
        self.name = None
        self.details = None
        logger.info("Deleted stream %s.", self.name)
    except:
        logger.exception("Couldn't delete stream %s.", self.name)
        raise


  def put_record(self, data, partition_key):
    try:
        response = self.kinesis_client.put_record(
            StreamName=self.name, Data=json.dumps(data), PartitionKey=partition_key
        )
        logger.info("Put record in stream %s.", self.name)
    except:
        logger.exception("Couldn't put record in stream %s.", self.name)
        raise
    else:
        return response

  def get_records(self, max_records):
    try:
        response = self.kinesis_client.get_shard_iterator(
            StreamName=self.name,
            ShardId=self.details["Shards"][0]["ShardId"],
            ShardIteratorType="LATEST",
        )
        shard_iter = response["ShardIterator"]
        record_count = 0
        while record_count < max_records:
            response = self.kinesis_client.get_records(
                ShardIterator=shard_iter, Limit=10
            )
            shard_iter = response["NextShardIterator"]
            records = response["Records"]
            logger.info("Got %s records.", len(records))
            record_count += len(records)
            yield records
    except:
        logger.exception("Couldn't get records from stream %s.", self.name)
        raise