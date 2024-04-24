#####################################################
#             TEMPORARY FILE!!!!!!                  #
#                 EDIT FIRST!!                      #
#####################################################

#1. Import OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, Bedrock-LLM
import os
import boto3
import json
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms.bedrock import Bedrock

# #5c. Wrap within a function
# def hr_index():
#     #2. Define the data source and load data with PDFLoader(https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf)
#     # data_load=PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')
#     with open('output.txt', 'r') as file:
#         data_load = file.read()
#     #3. Split the Text based on Character, Tokens etc. - Recursively split by character - ["\n\n", "\n", " ", ""]
#     data_split=RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=100,chunk_overlap=10)
#     #4. Create Embeddings -- Client connection
#     data_embeddings=BedrockEmbeddings(
#     credentials_profile_name= 'default',
#     model_id='amazon.titan-embed-text-v1',
#     region_name="us-east-1")
    
#     #5à Create Vector DB, Store Embeddings and Index for Search - VectorstoreIndexCreator
#     data_index = VectorstoreIndexCreator(
#         text=data_load,  # Pass the text data directly here
#         text_splitter=data_split,
#         embedding=data_embeddings,
#         vectorstore_cls=FAISS
#     )
    
#     return data_index

# #6a. Write a function to connect to Bedrock Foundation Model - Claude Foundation Model
# def hr_llm():
#     llm=Bedrock(
#         credentials_profile_name='default',
#         region_name="us-east-1",
#         model_id='anthropic.claude-v2',
#         model_kwargs={
#         "max_tokens_to_sample":3000,
#         "temperature": 0.1,
#         "top_p": 0.9})
#     return llm
# #6b. Write a function which searches the user prompt, searches the best match from Vector DB and sends both to LLM.
# def hr_rag_response(index,question):
#     rag_llm=hr_llm()
#     hr_rag_query=index.query(question=question,llm=rag_llm)
#     return hr_rag_query
# # Index creation --> https://api.python.langchain.com/en/latest/indexes/langchain.indexes.vectorstore.VectorstoreIndexCreator.html

def split_text_into_list(txt_file_path):
    # Open the text file
    with open(txt_file_path, 'r') as file:
        # Read the content of the file and split it into lines
        lines = file.readlines()
        
        # Remove leading and trailing whitespace from each line and store it in a list
        rows = [line.strip() for line in lines]
        
    return rows

# Setup bedrock
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)

sentences = split_text_into_list('output.txt')

def claude_prompt_format(prompt: str) -> str:
    # Add headers to start and end of prompt
    return "\n\nHuman: " + prompt + "\n\nAssistant:"

# Call Claude model
def call_claude(prompt):
    prompt_config = {
        "prompt": claude_prompt_format(prompt),
        "max_tokens_to_sample": 4096,
        "temperature": 0.5,
        "top_k": 250,
        "top_p": 0.5,
        "stop_sequences": [],
    }

    body = json.dumps(prompt_config)

    modelId = "anthropic.claude-v2"
    accept = "application/json"
    contentType = "application/json"

    response = bedrock_runtime.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )
    response_body = json.loads(response.get("body").read())

    results = response_body.get("completion")
    return results

def rag_setup(query):
    embeddings = BedrockEmbeddings(
        client=bedrock_runtime,
        model_id="amazon.titan-embed-text-v1",
    )
    local_vector_store = FAISS.from_texts(sentences, embeddings)

    docs = local_vector_store.similarity_search(query)
    context = ""

    for doc in docs:
        context += doc.page_content

    prompt = f"""Use the following pieces of context to answer the question at the end.

    {context}

    Question: {query}
    Answer:"""

    return call_claude(prompt)