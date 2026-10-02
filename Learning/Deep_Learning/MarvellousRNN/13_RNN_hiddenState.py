words = ["food","was","not","good"]

hidden_state ="empty memory"

print("Input Tokens :",words)

print("Initial hidden state :",hidden_state)

for index , word in enumerate(words):
    print("TimeStep : ",index+1)
    print("Current word :",word)
    print("Previous Memory :",hidden_state)

    hidden_state = "Memory after Reading :" + " ".join(words[:index+1]) + " "
    print("Updated Memory : ",hidden_state)

    print("-"*30)