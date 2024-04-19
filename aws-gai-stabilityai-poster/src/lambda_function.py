import json
import boto3
import base64
import datetime

# Create client connection with Bedrock and S3 Services
client_bedrock = boto3.client('bedrock-runtime')
client_s3 = boto3.client('s3')

def lambda_handler(event, context): 
    # Store the input data (prompt) in a variable
    input_prompt = event['prompt']

    # Create a Request Syntax to access the Bedrock Service 
    response_bedrock = client_bedrock.invoke_model(
        contentType='application/json', 
        accept='application/json',
        modelId='stability.stable-diffusion-xl-v0',
        body=json.dumps({"text_prompts": [{"text": input_prompt}],
                         "cfg_scale": 10,
                         "steps": 30,
                         "seed": 0}))
       
    # Retrieve from dictionary and convert streaming body to byte using json load
    response_bedrock_byte = json.loads(response_bedrock['body'].read())

    # Retrieve data with artifact key, import Base 64 and decode from Base64
    response_bedrock_base64 = response_bedrock_byte['artifacts'][0]['base64']
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)
    
    # Upload the File to S3 using Put Object Method
    poster_name = 'posterName'+ datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
        
    client_s3.put_object(
        Bucket='<BUCKET_NAME>',
        Body=response_bedrock_finalimage,
        Key=poster_name)

    # Generate Pre-Signed URL 
    generate_presigned_url = client_s3.generate_presigned_url(
        'get_object', 
        Params={'Bucket':'<BUCKET_NAME>','Key':poster_name}, 
        ExpiresIn=3600)
        
    return {
        'statusCode': 200,
        'body': generate_presigned_url
    }