def inlocuire():
    sir = input()
    sirnou = ""
    for caracter in sir:
        if caracter in 'aeiou':
            sirnou += caracter.upper() #sirnou = sirnou + caracter.upper()
            print(caracter.upper())
        else:
            sirnou += caracter #sirnou = sirnou + caracter
            print(caracter)
    print(sirnou)


def schimbarecuvant():
    cuvant = input()
    index = 0
    cuvantnou = ''
    for caracter in cuvant:
        if index == 0:
            cuvantnou += caracter.upper()
            print(caracter.upper(), 'am gasit primul element', index)
        else:
            if index == len(cuvant)-1:
                cuvantnou += caracter.upper()
                print(caracter.upper(), 'am gasit ultimul element', index)
            else:
                cuvantnou += caracter
                print(caracter, index)
        index += 1
    print(cuvantnou)


def halfsort():
    lista = [34, 0, 2, 5, 3, 300, 56]
    jumatate = len(lista) // 2
    print(len(lista), jumatate)
    list1 = lista[:jumatate:]
    print(list1)
    list1.sort()
    print(list1)
    list2 = lista[jumatate::]
    print(list2)
    list2.sort(reverse=True)
    print(list2)
    lista.sort()
    print(lista)
    lista.append(33)
    print(lista)
    print(lista.pop())
    print(lista)


if __name__ == "__main__":
   halfsort()