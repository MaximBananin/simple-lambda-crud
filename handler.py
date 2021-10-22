import logging
from services import create_item, update_item, delete_item, get_item_list
from services import build_response_json, check_correctness_params



logger = logging.getLogger("handler_logger")
logger.setLevel(logging.INFO)


def main_handler(event, context):
    response = 'Successfull'
    status = 500

    logger.debug("New request.")
    method = event['httpMethod']
    data = event['queryStringParameters']

    if data and not check_correctness_params(data):
        status = 400
        response = 'Bad Request'
        return build_response_json(status, response)


    if method == 'GET':
        response = get_item_list()

    elif method == 'PUT':
        if create_item(data):
            status = 201

    elif method == 'DELETE':
        if delete_item(data):
            status = 200

    elif method == 'PATCH':
        if update_item(data):
            status = 200

    else:
        response = 'Method is not allowed'
        status = 405

    logger.debug("Make response.")
    return build_response_json(status, response)
