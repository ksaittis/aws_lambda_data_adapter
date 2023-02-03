import os
import boto3
import requests

def lambda_handler(event, context):
    sqs = boto3.client("sqs")
    queue_url = os.environ.get("SQS_QUEUE")
    destination_endpoint = os.environ.get("DESTINATION_ENDPOINT")
    
    # Receive message from SQS queue
    sqs_message = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=["All"],
        MaxNumberOfMessages=1,
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    
    # Get the message from the response
    message = sqs_message["Messages"][0]
    payload = message["Body"]
    
    # Send the payload to the endpoint
    requests.post(destination_endpoint, json=payload)
    
    # Delete the message from the SQS queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message["ReceiptHandle"]
    )
