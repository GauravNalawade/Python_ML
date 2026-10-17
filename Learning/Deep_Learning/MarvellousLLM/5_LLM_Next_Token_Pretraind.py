import torch 

from transformers import AutoTokenizer
from transformers import AutoModelForCasualLM

# pretrained model name
model_name = "distilgpt2"

# Load Tokenizer 
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load pretrained languge model
model = AutoModelForCasualLM.from_pretrained(model_name)

# Input promt 
promt ="I Love"

# Convert Input into token ids 
inputs = tokenizer(
    promt,
    return_tensors = "pt"
)

# Enable Evaluation mode
model.eval()

# perform inference without gradient calculations 
with torch.no_grad():
    outputs = model(**inputs)

# Extract logits for final input position 
logits = outputs.logits[0,-1,:]

# Convert logits into probabilities 
probabilities = torch.softmax(
    logits,
    dim=-1
)

# select five highest proababilities tokens 
values , indices = torch.topk( 
    probabilities,
    5
) 

print("Input :",promt)
for value,index in zip(values,indices):
    token = tokenizer.decode([index.item()])
    print(repr(token), round(value.item(),4))

