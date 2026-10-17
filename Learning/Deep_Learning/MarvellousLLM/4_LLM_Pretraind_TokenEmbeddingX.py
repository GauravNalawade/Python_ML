import torch 

from transformers import AutoTokenizer
from transformers import AutoModelForCasualLM

# pretrained model name
model_name = "distilgpt2"

# Load Tokenizer 
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load pretrained languge model
model = AutoModelForCasualLM.from_pretrained(model_name)

# Input Sentance
sentance ="India is my country" 

# Convert Text into Pytorch tensors 
inputs = tokenizer(
    sentance,
    return_tensors = "pt"
)

# Extract TokenID
token_ID = inputs["input_ids"]

# Access the pretrained input embedding layer
embedding_layer = model.get_input_embeddings()

# Retrieve the Embeddign Vector 
embeddings = embedding_layer(token_ID)

print("Input Sentance : ",sentance)

print("Token IDs : ")
print(token_ID)

print("Embedding shape : ")
print(embeddings.shape)

print("First token embedding :")
print(embeddings[0,0, :10])