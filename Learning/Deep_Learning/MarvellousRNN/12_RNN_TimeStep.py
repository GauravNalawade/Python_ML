sentance = "food was not good"
# TimeStep   1    2   3   4
# Token      1    2   5   3
# Embeding  [0.1,0.9]  [0.1,0.9]   [0.1,0.9]   [0.1,0.9]  

words = sentance.split()

print("Actual sentance is :",sentance)

for index, word in enumerate(words):
    print("TimeStep : ",index+1, ":",word) 