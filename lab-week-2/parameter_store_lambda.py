import json
import boto3

def lambda_handler(event, context):
    parameter_name = "demo"
    # Create a System Manager client
    session = boto3.session.Session()
    client = session.client(service_name='ssm')
    
    # Get secret from System Manager
    parameter = client.get_parameter(Name=parameter_name, WithDecryption=True)
        
    print(parameter['Parameter']['Value'])