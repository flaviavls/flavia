def adunare2():
    print('Introduceti va rog un numar de 2 cifre:')
    a = int(input())
    z = a // 10
    u = a % 10
    print('Numarul rezultat prin adunarea zecilor si unitatilor este:', z+u)


def adunare3():
    print('Introduceti va rog un numar de 3 cifre:')
    a = int(input())
    s = a // 100
    z = a // 10 % 10
    u = a % 10


def capetesipicioare():
    print("Introduceti va rog numar de oi:")
    o = int(input())
    print("Introduceti va rog numar de gaini")
    g = int(input())
    print("Numarul de capete este:", g+o, ", iar numarul de picioare este:", 2*g+4*o)


def eliminare():
    print('Introduceti va rog un numar de 3 cifre:')
    a = int(input())
    s = a // 100
    z = a // 10 % 10
    u = a % 10
    print('Numarul rezultat prin eliminarea cifrei zecilor este:', str(s)+str(u))


def gauss():
    print("Introduceti numarul(natural) pentru care se doreste calcularea sumei lui Gauss:")
    n = int(input())
    print("Suma lui Gauss este:", n*(n+1)//2)


def ora():
    print('Introduceti ora:')
    h = int(input())
    print('Introduceti minutele:')
    n = int(input())
    print('Introduceti numarul de minute ccare se vor aduna la ora si minutele introduse anterior:')
    x = int(input())
    ov = h*60+n*x #ora viitoare exprimata in minute
    print('Ora va fi:', ov//60, 'si minute', ov%60)


if __name__ == "__main__":
    adunare2()
    adunare3()
    capetesipicioare()
    eliminare()
    gauss()
    ora()