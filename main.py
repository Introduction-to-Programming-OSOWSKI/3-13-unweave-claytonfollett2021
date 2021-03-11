def unweave(w):
    newWord1 = ""
    newWord2 = ""
    for i in range(0, len(w), 2):
        newWord1 = newWord1 + w[i] 

    for i in range (1, len(w), 2):
        newWord2 = newWord2 + w[i]
    
    return newWord1 + " " + newWord2

print (unweave("potato"))