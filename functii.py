sm = 0

def adunarecametoda(*args):
    global sm
    for a in args:
        sm += a


def adunare(*a):
    s = 0
    for element in a:
        s = s + element
    return s

def adunare2lista(lista):
    listanoua = list()
    for i in range(len(lista)):
        listanoua.append(lista[i]+2)
    return listanoua

# primul parametru este o lista de numere intregi
# al doilea parametru reprezinta valoarea initiala a sumei finale si rezultatul functiei sale
def adunarelista(lista, s=0):
    # aici execut o parcurgere a listei de intrare
    for i in range(len(lista)):
        s += lista[i]
    return s


def inmultire2lista(lista):
    listanoua = list()
    for i in range(len(lista)):
        listanoua.append(lista[i]*2)
    return listanoua

def oglindit(n):
    return int(str(n))[::-1]


# verificare numar prim
def verificareprime(numar):
    # daca numarul este 2 atunci este un numar prim
    if numar == 2:
        return True
    #daca este mai mic ca si 2 atunci nu este prim
    if numar < 2:
        return False
    #daca numarul se imparte exact la 2 atunci nu este prim
    if numar % 2 == 0:
        return False
    #luam numerele de la 3 pana la valoarea numarului impartit la 2
    for divizor in range(3, numar // 2):
        #daca numarul se imparte la divizor atunvi nu e prim
        if numar % divizor == 0:
            return False
    #daca s-a ajuns aici inseamna ca numarul meu este prim
    return True


#gasirea primului numar prim mai mare ca si n
def nr_prim(numar):
    # am nevoie de o variabila care sa imi spuna ca am gasit numarul prim
    # initializezz variabila respectiva cu false sau 0
    gasit = 0
    # cat timp nu am gasit numarul
    while gasit == 0:
        # maresc numarul meu cu 1 si verific daca este prim
        numar = numar + 1
        # daca este prim modific variabile gasit in true, prin urmare while-ul se va opri
        if verificareprime(numar):
            gasit = 1
        #reintorc numarul gasit
        return numar


#opt poate lua valori 1, 2 sau 3, unde 1-adunare, 2=scadere, 3-produs
def meniu3(opt): # specificam tipul parametrului/lor si ce reprezinta fiecare parametru
    if opt == 1:
        return "adunare"
    elif opt == 2:
        return "scadere"
    elif opt == 3:
        return "inmultire"
    else:
        return "operatie nedefinita"


def cifrazero(n):
    # am definit numarul meu in sir de caractere
    str = str(n)
    # am initializat un contor cu 0
    contor = 0
    # pentru fiecare caracter in sirul meu
    for caracter in str:
        # verific daca este 0, iar daca da implementez contorul
        if caracter == "0":
            contor += 1
        # intorc ca si rezultat al functiei contorul definit de mine
        return contor


# produsul unor numere primite ca parametru de o functie
def produsul(*args):
    p = 1
    for a in args:
        p = p * a
    return p


# factorialul unui numar n, n!
def factorial(n):
    f = 1
    i = 1
    # varianta cu while
    while i<=n:
        f = f*i
        i = i+1
        # varianta cu for
    for i in range(1, n+1):
        f = f*1
    return f

if __name__ == "__main__":
    #v1 = adunare(s=1, 1,2,3)
    #v2 = adunare(3)
    #v3 = adunare()
    #print(v3)
    #print(adunare(v1,v2))
    #adunarecametoda(1, 2, 4, 5)
    #print(sm)
    #print(adunare(1, 2, 4, 5))
    #print(adunare2lista([1,2,3,4]))
    #print(inmultire2lista([1,2,3,4]))
    #print(oglindit(123456))
    #s1 = 10
    #print(adunarelista[1,2,3,4], s1)
    #print(cifrazero(1,2,3,4))
    print(cifrazero())


