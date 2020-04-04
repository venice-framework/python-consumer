from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError

import os
import time

"""
This is an example consumer intended to demonstrate basic
functionality of the pipeline.

This consumer subscribes to a topic, deserializes events (messages),
and prints them out.

You must set the TOPIC_NAME environment variable.
This image does not have a default TOPIC_NAME set, to avoid
potentially confusing errors.

Reference: https://github.com/confluentinc/confluent-kafka-python
"""

BROKER = os.environ['BROKER']
SCHEMA_REGISTRY_URL = os.environ['SCHEMA_REGISTRY_URL']
TOPIC_NAME = os.environ['TOPIC_NAME'] 

c = AvroConsumer({
    'bootstrap.servers': BROKER,
    'group.id': 'groupid',
    'schema.registry.url': SCHEMA_REGISTRY_URL})

c.subscribe([TOPIC_NAME])

while True:
    try:
        # block for 10s max waiting for message
        msg = c.poll(timeout=10)

    except SerializerError as e:
        # Report malformed record, discard results, continue polling
        print("Message deserialization failed for {}: {}".format(msg, e))
        break

    # There were no messages on the queue, continue polling
    if msg is None:
        continue

    if msg.error():
        print("AvroConsumer error: {}".format(msg.error()))
        continue

    print(msg.value())
    print(msg.key())

c.close()