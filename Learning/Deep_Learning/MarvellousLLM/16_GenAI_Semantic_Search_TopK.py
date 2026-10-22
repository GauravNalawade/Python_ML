from sentence_transformers import SentenceTransformer,util

# load pre-trained Embeddig model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Knowledge Base
Documents = [
    "python is used for machine learning",
    "java is used for enterprise application",
    "SQL is used to manage databases",
    "HTML is used to create webpages",
    "Tensorflow is used for Deeplearning"
]

# Generate Document Embedding
documents_embedding = model.encode(Documents,convert_to_tensor=True)

# Accept Question 
query = input("Enter your question ")

# Generate query Embedding
query_embedding = model.encode(query,convert_to_tensor=True)

# Calculate similarity
scores= util.cos_sim(query_embedding,documents_embedding)[0]

# find top 2 matching documents
top_result = scores.topk(2)

print("Top 2 Releavent Documtes : ")

for index in top_result.indices:
    print(Documents[index.item()]) 