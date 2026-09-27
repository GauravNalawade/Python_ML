sentences = [
        "food was good",
        "food was bad",
        "food was not good"
]

vocablary = []

for sentence in sentences:
    words = sentence.split()

    for word in words:
        if word not in vocablary:
            vocablary.append(word) 

for index , x in enumerate(vocablary): 
    print("Position : ",index+1,":",x)  