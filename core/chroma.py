import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.HttpClient(port=8010)
default_ef = embedding_functions.DefaultEmbeddingFunction()
chroma_collection = chroma_client.get_or_create_collection(name="creators", embedding_function=default_ef)
