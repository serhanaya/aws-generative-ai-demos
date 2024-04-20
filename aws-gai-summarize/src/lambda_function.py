import json
import boto3

# Create client connection with bedrock
client_bedrock=boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    input_prompt=event['prompt']
   
    # Create Request
    client_bedrockrequest=client_bedrock.invoke_model(
       contentType='application/json',
       accept='application/json',
       modelId='cohere.command-light-text-v14',
       body=json.dumps( {
        "prompt": input_prompt,
        "temperature": 0.5,
        "p": 0.8,
        "k": 0,
        "max_tokens": 100}))

    # Convert Streaming Body
    client_bedrock_byte=client_bedrockrequest['body'].read()

    client_bedrock_string=json.loads(client_bedrock_byte)

    # Update the 'return' by changing the 'body'
    client_final_response=client_bedrock_string['generations'][0]['text']
    print(client_final_response)

    return {
        'statusCode': 200,
        'body': json.dumps(client_final_response)
    }