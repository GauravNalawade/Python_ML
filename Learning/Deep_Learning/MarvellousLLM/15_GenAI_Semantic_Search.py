from sentence_transformers import SentenceTransformer
from sentence_transformers import util

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

# Display scores
for index,score in  enumerate(scores):
    print(Documents[index]," : ",score.item())

# Find the best document 
best_index = scores.argmax().item()

print("Most Relevant Document :")
print(Documents[best_index]) 