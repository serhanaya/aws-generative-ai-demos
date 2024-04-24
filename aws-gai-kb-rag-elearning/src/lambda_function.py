import boto3

# 1. create client connection with bedrock
client_bedrock_knowledgebase = boto3.client('bedrock-agent-runtime')

def lambda_handler(event, context):
    # 2. Store the user prompt
    user_prompt=event['prompt']

    # 3. Use retrieve and generate API
    client_knowledgebase = client_bedrock_knowledgebase.retrieve_and_generate(
    input={
        'text': user_prompt
    },
    retrieveAndGenerateConfiguration={
        'type': 'KNOWLEDGE_BASE',
        'knowledgeBaseConfiguration': {
            'knowledgeBaseId': '<KNOWLEDGE_BASE_ID>',
            'modelArn': 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-instant-v1'
                }
            })
        
    # 4. Store the response
    response_kbase_final=client_knowledgebase['output']['text']
    
    # 5. Return the response
    return {
        'statusCode': 200,
        'body': response_kbase_final
    }