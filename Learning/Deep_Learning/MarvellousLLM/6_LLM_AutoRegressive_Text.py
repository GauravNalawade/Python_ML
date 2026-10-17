from transformer import pipeline 

# Load pre-trained text generation pipeline
generator = pipeline(
    "text-generation",
    model = "distilgpt2"
) 

# input prompt 
prompt = "Artificial intelligence is"

# Generate Text 
result = generator(
    prompt,
    max_new_tokens = 30,
    do_sample = False,
    pad_token_id = generator.tokenizer.eos_token_id
)

print("Generated Text : ")
print(result[0]["generated_text"])

