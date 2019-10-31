import boto3

session = boto3.Session(profile_name='bharathraju')

s3client = session.client('s3')

response = s3client.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List:  %s" % buckets)

