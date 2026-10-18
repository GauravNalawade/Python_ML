from ollama import chat
import json 

# Prompt for LLM 
prompt = """Give me the infomation about python programming language.
Return thee result as JSON with this keys:
language 
type
creator
"""
response = chat(
    model="llama3.2:1b",
    messages=[
        {
        "role":"user",
        "content":prompt
        }
    ],
    format="json"
)

answer=response.message.content
print("LLM Response :")
print(answer) 

# Convert JSON string to python dictonary
data= json.loads(answer)

print("Data from dictonary is :",data)

print("Data from Dictonary")

print("language:",data.get("language"))
print("type:",data.get("type")) 
print("creator:",data.get("creator"))
