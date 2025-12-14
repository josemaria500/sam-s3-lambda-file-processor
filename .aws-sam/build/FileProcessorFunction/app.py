import json
import os
import boto3

def lambda_handler(event, context):
    record = event["Records"][0]
    bucket_name = record["s3"]["bucket"]["name"]
    object_key = record["s3"]["object"]["key"]
    object_size = record["s3"]["object"]["size"]

    file_extension = object_key.split(".")[-1] if "." in object_key else "unknown"

    processed_data = {
        "bucket": bucket_name,
        "file_name": object_key,
        "size_bytes": object_size,
        "extension": file_extension
    }

    # Detectar ejecución local
    if os.environ.get("AWS_SAM_LOCAL") == "true":
        print("Running locally, skipping S3 write")
        return {
            "statusCode": 200,
            "body": processed_data
        }

    # Ejecución real en AWS
    s3 = boto3.client("s3")
    output_bucket = os.environ["OUTPUT_BUCKET"]
    output_key = f"processed/{object_key}.json"

    s3.put_object(
        Bucket=output_bucket,
        Key=output_key,
        Body=json.dumps(processed_data),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": processed_data
    }
