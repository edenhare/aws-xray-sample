import json
import random

def lambda_handler(event, context):

    random.seed()
    number = random.randint(0,1)
    if number == 0:
        status = 200
        text = "ok"
    else:
        status = 400
        text = "bad"

    result =  {
        'statusCode': status,
        'body': {
            'text': text,
            'first': event['body']['first'],
            'second': event['body']['second'],
        }
    }

    return result
