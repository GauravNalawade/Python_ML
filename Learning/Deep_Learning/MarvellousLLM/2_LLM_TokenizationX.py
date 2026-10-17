from transformers import AutoTokenizer

#  Load Pre-Trained Tokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Input Sentance
sentance = "python is easy programming language I Love it"

# Convert the sentance into tokens 
tokens = tokenizer.tokenize(sentance)

token_ids = tokenizer.encode(
    sentance,
    add_special_tokens =False,

)


# Convert TokenID back to text
decoded = tokenizer.decode(token_ids)

print("Original Sentance : ",sentance)

print("Tokens IDs : ",token_ids)

print("Decoded sentance : ",decoded)

