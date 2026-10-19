from sentence_transformers import SentenceTransformer

# load pre-trained Embeddig model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "python is a programming language",
    "python is used for data science",
    "I support indian cricket team"
]

embeddings = model.encode(sentences)

# Display sentence embedding 
for index, embeddig in enumerate(embeddings):
    print("-"*40)
    print("\n sentence: ",sentences[index])

    print("Embedding :")
    print(embeddig)

    print("Total dimension :",len(embeddig))
    