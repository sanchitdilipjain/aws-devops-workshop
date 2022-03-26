import boto3


def lambda_handler(event, context):
    secret_name = "demo"
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')
    
    # Get secret from Secrets Manager
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        
    print (get_secret_value_response['SecretString'])