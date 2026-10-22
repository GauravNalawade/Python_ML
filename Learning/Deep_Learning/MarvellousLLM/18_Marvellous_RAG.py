import chromadb 
from sentence_transformers import SentenceTransformer,util
from ollama import chat


# load pre-trained Embeddig model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to existng chromaDB 
client = chromadb.PersistentClient(path="./MarvellousDB")

collection = client.get_collection(name="marvellous_knowledge")

# Accept Question 
query = input("Enter your question ")

# Generate query Embedding
query_embedding = model.encode(query,convert_to_tensor=True) 

# Retrieve top 2 Relevent results 
results = collection.query(query_embeddings=[query_embedding.tolist()],n_results=2) 

# Create context from retrieved Documents 
documents = results["documents"][0]

context = "\n".join(documents)
print("Retrived Context :")
print(context)

