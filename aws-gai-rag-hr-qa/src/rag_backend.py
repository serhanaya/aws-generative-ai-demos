from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain_aws.llms.bedrock import BedrockLLM


def create_hr_index():
    """Creates an index for the HR policy document."""

    # Load the HR policy document
    data_loader = PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')

    # Split the text into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""], 
        chunk_size=100, 
        chunk_overlap=10)

    # Create embeddings for the text chunks
    embeddings = BedrockEmbeddings(
        credentials_profile_name='default', 
        model_id='amazon.titan-embed-text-v1')

    # Create a vector database and index for the embeddings
    index_creator = VectorstoreIndexCreator(
        text_splitter=text_splitter, 
        embedding=embeddings, 
        vectorstore_cls=FAISS)
    
    index = index_creator.from_loaders([data_loader])

    return index

def create_hr_llm():
    """Creates a connection to the Bedrock LLM."""

    llm = BedrockLLM(
        credentials_profile_name='default', 
        model_id='anthropic.claude-v2', 
        model_kwargs={
        "max_tokens_to_sample":3000,
        "temperature": 0.1,
        "top_p": 0.9})

    return llm


def get_hr_rag_response(index, question):
    """Gets a response from the LLM based on a user prompt and the HR policy document."""

    llm = create_hr_llm()
    rag_query = index.query(question=question, llm=llm)

    return rag_query