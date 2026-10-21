def lambda_handler(event, context):

    token = event.get("authorizationToken")

    if token == "allow":
        effect = "Allow"
    else:
        effect = "Deny"

    return {
        "principalId": "user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": event["methodArn"]
                }
            ]
        }
    }