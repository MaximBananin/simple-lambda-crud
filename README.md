# simple-lambda-crud
Simple CRUD backend for AWS-lambda


Install guide:

  1. deploy in your AWS
  '''serverless deploy'''
  2. Create table DynamoDB.
  3. Put name new base in environment
  '''TABLE_NAME: *name* '''


Use guide:

  Function 'main_handler' take HTTP request.
  Allowed methods:
    GET - get all Items
    PUT - create new Item. Required 'content'  
    PATH - update Item. Required 'index'  
    DELETE - Delete Item. Required 'index'
