def factor_interes(slide1, slide2):
    esta = 0
    for i in slide1[1]:
        if i in slide2[1]:
            esta += 1

    return min([esta, len(slide1[1])-esta, len(slide2[1])-esta])

lista1 = [1,['cat', 'beach', 'sun']]
lista2 = [2,['hola', 'mañana']]

print(factor_interes(lista1, lista2))
    
