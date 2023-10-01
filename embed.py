import os
import sys
import time

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Import necessary modules
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import TextLoader, UnstructuredMarkdownLoader
from langchain.memory import ConversationBufferMemory

#here onwords is vijay
print("runnning")

def add_to_vdb(file_path):
    # Open and read the Markdown file
    with open("./docs/" + file_path, "r", encoding="utf-8") as md_file:
        markdown_content = md_file.read()

    markdown_document = markdown_content
    #documents needs to be text spliter

    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3")
    ]

    # MD splits
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    md_header_splits = markdown_splitter.split_text(markdown_document)

    # Char-level splits
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    chunk_size = 1000
    chunk_overlap = 200
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    # Split
    splits = text_splitter.split_documents(md_header_splits)
    documents = splits

    if len(documents) != 0:
        

        # Initialize embeddings and vector store
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents, embeddings)

        # Define the directory where you want to save the persisted database
        persist_directory = 'db4'

        # Initialize OpenAIEmbeddings for embedding
        embedding = OpenAIEmbeddings()

        # Create and persist the Chroma vector database
        vectordb = Chroma.from_documents(documents=documents, embedding=embedding, persist_directory=persist_directory)

        # Persist the database to disk
        vectordb.persist()
    else:
        print("ERROR!!")

if __name__ == "__main__":
    l = os.listdir("./docs/")

    for i in range(len(l)):
        print("Running:", i, "of", len(l))
        add_to_vdb(l[i])
        time.sleep(5)

    print("done done")