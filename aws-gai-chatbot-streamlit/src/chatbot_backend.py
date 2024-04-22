import logging
from langchain_aws.llms.bedrock import BedrockLLM
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

MODEL_ID = 'meta.llama2-70b-chat-v1'
CREDENTIALS_PROFILE = 'default'  
MODEL_KWARGS = {
    "temperature": 0.5,
    "top_p": 0.5,
    "max_gen_len": 512
}

def load_llm():
    """Loads the Bedrock LLM with specified configuration.

    Returns:
        Bedrock: The initialized Amazon Bedrock language model.
    """

    try:
        return BedrockLLM(
            credentials_profile_name=CREDENTIALS_PROFILE,
            model_id=MODEL_ID,
            model_kwargs=MODEL_KWARGS
        )
    except Exception as e:
        logging.error(f"Error loading LLM: {e}")
        raise

def create_memory():
    """Creates a ConversationBufferMemory object.

    Returns:
        ConversationBufferMemory: The initialized memory object.
    """

    llm = load_llm()
    return ConversationBufferMemory(llm=llm, max_token_limit=512)

def create_conversation_chain():
    """Creates a ConversationChain object.

    Returns:
        ConversationChain: The initialized conversation chain.
    """

    llm = load_llm()
    memory = create_memory()
    return ConversationChain(llm=llm, memory=memory, verbose=True)

def get_chat_response(input_text):
    chain = create_conversation_chain()
    try:
        response = chain.run("The following is a conversation with a helpful and informative chatbot. Only provide the chatbot's response. Do not include 'Human:' or 'AI:' in your responses.\nChatbot: " + input_text + "\nAnswer: ")
        return response
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return "Sorry, I'm having trouble understanding. Can you try again?"
