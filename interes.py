import random as r

def factor_interes(slide1, slide2):
    esta = 0
    for i in slide1[1]:
        if i in slide2[1]:
            esta += 1

    return min([esta, len(slide1[1])-esta, len(slide2[1])-esta])

def enlazar():
    global slides
    salida = []

    salida.append(slides.pop(r.randint(0, len(slides)-1)))

    while len(slides) > 1:
        encontrado = False

        for i in slides:
            if not encontrado:
                if factor_interes(salida[-1], i) > interes:
                    salida.append(i)
                    slides.remove(i)
                    encontrado = True

    salida.append(slides[0])

    return salida
