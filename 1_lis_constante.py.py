def f_lerNum(lista):
    lista=[]
    while True:
        num = int(input())
        if num != 0:
            lista.append(num)
        else: break
    return lista

def f_multipConstante(lista):
    lista2 = lista[:]
    constante = int(input())
    for i in range (len(lista)):
        lista2[i] *= constante
    return lista2
    
def main():
    listaA = []
    listaB = f_lerNum(listaA)
    listaC = f_multipConstante(listaB)

    print(listaC)
    
if __name__=="__main__":
    main()
