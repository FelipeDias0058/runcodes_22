import math

def soma_cumulativa(lista):
    lista2 = []
    total = 0
    for n in lista:
        total += n
        lista2.append(total)
    return lista2


def main():
    lista = []
    while True:
        num = float(input())
        if num == 0: break
        lista.append(num)
        
    lista_acc = soma_cumulativa(lista)
    lista_acumulada = [math.trunc(x) for x in lista_acc]

    print(lista_acumulada)

if __name__ == '__main__':
    main()
