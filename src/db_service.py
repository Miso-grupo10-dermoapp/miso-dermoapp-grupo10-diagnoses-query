import boto3
from boto3.dynamodb.conditions import Attr

import app

def get_item(patient_id, case_id):
    client = boto3.resource('dynamodb')
    try:
        table = client.Table(app.ENV_TABLE_NAME)
        result = table.scan(
              Select= 'ALL_ATTRIBUTES',
              FilterExpression=Attr('patient_id').eq(patient_id) & Attr('case_id').eq(case_id)
              )
        items = result['Items']
        if items:
            return items
        else:
            return []
    except Exception as e:
        raise RuntimeError('cannot retrieve data from db cause: ' + str(e))
