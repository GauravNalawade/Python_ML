from ollama import chat 


# Select the local LLM
Model = "llama3.2:1b"

# define prompts
prompts = [
    "Explain recursion",

    "Explain recursion in python in 3 simple points",

    """ You are experienced python teacher.
    Explain recursion for beginner.
    Give one simple example.""",

    """Convert programming languages to uppercase.
    Exaple 1: 
    Input: python
    Output:PYTHON

    Exaple 2: 
    Input: java
    Output:JAVA

    Exaple 3: 
    Input: javascript
    Output:""

    """
]

# Execute Every prompt 
for index, prompt in enumerate(prompts, start=1):
    print("-"*30)
    print("Prompt number :",index)
    print("Input Prompt :",prompt)

    response = chat(
        model=Model,
        messages=[
            {
            "role":"user",
            "content":prompt
            }
        ]
    )

    print("\n Response from LLM is :")
    print(response.message.content) 