import os
import time

'''
class Dictionary:
    def __init__(self, ):
        self.own_dic = create_dic(raw_matrix)


    def create_dic(mtx):

'''

'''
[
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]],
['char',[list]]
]
'''

def depurate(mtx):
    dic = []
    for elem in mtx:
        for tag in elem[1]:
            encontrado = False
            for word in dic:
                if tag == word[1]:
                    encontrado = True
                    word[0]+=1
                    break
            if encontrado:
                continue
            else:
                dic.append([1,tag])

    print("Dictionary Created. \n")

    for word in dic:
        if word[0] == 1:
            for elem in mtx:
                if word[1] in elem[1]:
                    elem[1].remove(word[1])
                    break

    print(dic)
    print(mtx)




def main():
    mtx = [['char',['1','4','5']], ['char',['3','5','4']], ['char',['1','2']]]
    depurate(mtx)
    PB = ProgressBar(300)
    i = 0
    while(PB.update(i) != 100.0):
        i+=1
        time.sleep(0.01)


if __name__ == '__main__':
    main()
