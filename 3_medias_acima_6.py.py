def fNotas(n):
    lista = []
    for i in range(n):
        lista.append(float(input()))
    return lista

def fMedia(lista):
    average = []
    for i in range(len(lista)):
        if 10.1 >lista[i] >=6:
            average.append(i)
    return average


def main():
    nota = fNotas(50)
    media_notas = fMedia(nota)
    print(media_notas)
    
if __name__=="__main__":
    main()
