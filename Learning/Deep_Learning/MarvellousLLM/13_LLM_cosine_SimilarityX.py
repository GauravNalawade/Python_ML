from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# load pre-trained Embeddig model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1= "python is a programming language"
sentence2= "I love to play cricket"

embedding1 = model.encode(sentence1,convert_to_tensor=True)
embedding2 = model.encode(sentence2,convert_to_tensor=True)

# Calculate cosin similariry
similarity = util.cos_sim(embedding1,embedding2)

print("Sentence1: ",sentence1)
print("Sentence2: ",sentence2)

print("Cosin Similariry:")
print(similarity.item())

