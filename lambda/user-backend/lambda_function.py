import json
import boto3

iam = boto3.client("iam")


def lambda_handler(event, context):

    body = json.loads(event["body"])

    user_name = body["userName"]

    iam.create_user(
        UserName=user_name
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": f"IAM user '{user_name}' created successfully"
        })
    }