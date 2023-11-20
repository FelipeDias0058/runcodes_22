#Lê o input n vezes e o adiciona à lista 
def f_lista():
    n = int(input().strip())
    lista = []
    for i in range(n):
        numeros = input().strip()
        lista.append(numeros)
    return lista

#Confere se a lista é ou não ordenada
def f_listaOrdenada(lista):
    if (isinstance(lista, list)):
        memoria = lista[1]

        if isinstance(memoria, str):
            if memoria.isnumeric():
                lista_ordenada = sorted(lista, key=float)
            else:
                lista_ordenada = sorted(lista, key=str)
        return lista_ordenada == lista

#Exibe a mensagem adequada na tela
def f_saidaDados(resultado):
    if (resultado):
        print('LISTA ORDENADA')
    elif (resultado == False):
        print('LISTA NÃO ORDENADA')


def main():
    lista = f_lista()
    resultado = f_listaOrdenada(lista)
    f_saidaDados(resultado)


if __name__ == '__main__':
    main()
