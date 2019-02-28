import random

def matching(photo1, photo2):
    matchingsi = 0
    for i in range(len(photo1[1])):
        for j in range(len(photo2 [1])):
            if(photo[1][i] == photo[1][j]):
                matchingsi+= 1
    return matchingsi

def emparejar (verticales):
    maximo = 1000000
    numrandom= random.randint(0,len(verticales)-1)
    random = verticales[numrandom]
    for i in range(0, len(verticales)-1):
        numero = matching(random, verticales[i])
        if numero < maximo:
            maximo = numero
            elegida = verticales[i]
            numeroelegida = i
    del verticales[numeroelegida]
    del verticales[numrandom]
    return elegida, random

def tags (photo1, photo2,tgmatch):
    tgmax = photo[0] + photo[0] - tgmatch
    vector[tgmax]
    tgmin = 0
    for i in range(len(photo1[1])):
        for j in range(len(photo2 [1])):
            if(photo[1][i] != photo[1][j]):
                vector[tgmax] = photo[1][i]
                tgma+=1
                vector[tgmax] = photo[1][j]
                tgmax+=1
            else:
                vector[tgmax] = photo[1][i]
                tgmax+=1
    return vector
                
