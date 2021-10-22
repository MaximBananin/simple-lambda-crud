import os
import time
import logging
import json
import boto3
from uuid import uuid4
from encoders import DecimalEncoder



TABLE_NAME = os.environ['TABLE_NAME']

logger = logging.getLogger("services_logger")
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)



def create_item(data):
    timestamp = int(time.time())
    index = str(uuid4())

    table.put_item(Item={
            "index": index,
            "timestamp": timestamp,
            "content": data['content']})

    logger.info("Create item.")
    return True


def update_item(data):
    timestamp = int(time.time())
    index = data['index']

    table.put_item(Item={
            "index": index,
            "timestamp": timestamp,
            "content": data['content']})

    logger.info("Update item.")
    return True


def delete_item(data):
    index = data['index']
    table.delete_item(Key={'index': index})

    logger.info("Delete item.")
    return True


def get_item_list():
    response = table.scan()
    data = response['Items']

    logger.info("Get all items.")
    return data


def check_correctness_params(data):
    ''' Check type for params '''

    index = data.get('index')
    content = data.get('content')
    result = False

    if index and isinstance(index, str):
        result = True

    if content:
        if isinstance(content, str):
            result = True
        else:
            result = False

    logger.info("Сhecking the correctness of parameters.")
    return result


def build_response_json(status, data):
    ''' Receives data and prepares a response   '''

    response = {
        "statusCode": status,
        "body": json.dumps(data, cls=DecimalEncoder)
    }
    logger.info("Build response.")
    return response
