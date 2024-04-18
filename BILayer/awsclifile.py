import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List objects in a bucket
bucket_name = 'your_bucket_name'
response = s3.list_objects_v2(Bucket=bucket_name)

# Print object keys
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("No objects found in the bucket.")
