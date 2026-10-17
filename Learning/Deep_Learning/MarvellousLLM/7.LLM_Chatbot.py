from ollam import chat

messages = [
    {
        "role": "system",
        "content": "You are a python programming student"
    }
]

print("Marvllous python Tutor")
print("Type exit to stop")

while True:
    # Accept user input
    question = input("\n You : ").strip()

    # Stop chat bot
    if question.lower() == "exit":
        print("Thank you for using Mavellous Bot")
        break

    # ignore empty line
    if not question:
        continue

    messages.aapend(
        {
            "role" :"user",
            "content" :"question"
        }
    )

    response = chat(
        model ="llama3.2:1B",
        messages=messages
    )

    answer =response.message.content

    print("\n Marvellous AI :",answer)

    messages.append({
        "role":"assistant",
        "content": answer
    })