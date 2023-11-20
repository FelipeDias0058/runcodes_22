def f_impar_par(n):
    return not n%2 == 0

def f_count_100(n):
    lista=[]
    for i in range(n):
        lista.append(int(input()))
        lista2 = sorted(lista)
    return lista2

def fMultiply(lista2, n):
    lista3 = lista2[:]
    for i in range(n):
        if f_impar_par(i)==0:
            lista3[i]*=3
            
        elif f_impar_par(i)!=0:
            lista3[i]*=5
    return lista3


def main():
    listaA = f_count_100(100)
    listaB = fMultiply(listaA,100)
    print(listaB)

if __name__=="__main__":
    main()
