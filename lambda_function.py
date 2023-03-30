import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
sns = boto3.client('sns')

def generate_presigned_url(bucket_name, object_name, expiration=300):
    try:
        response = s3.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        print(e)
        return None

    # The response contains the presigned URL
    return response

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_name = event['Records'][0]['s3']['object']['key']
    
    # Get the image URL
    image_url = generate_presigned_url(bucket_name, object_name)
   

    # Define the email HTML template with the image
    email_template = f"""{image_url}"""
    
    # Publish the email to the SNS topic
    topic_arn = 'arn:aws:sns:ap-south-1:730390155220:S3bucketTrigger'
    response = sns.publish(
        TopicArn=topic_arn,
        Message=email_template,
        Subject='My Email with an Image'
    )
    
    return {
        'statusCode': 200,
        'body': image_url
    }
