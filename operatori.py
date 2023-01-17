def sumanumere():
    print("Introduceti primul numar, a")
    a = input()
    print("Numarul introdus a=", a)
    print("Introduceti al 2-lea numar, b")
    b = input()
    print("Numarul introdus b=", b)
    print("a+b = ", int(a)+int(b))


def scaderenumere():
    print("Introduceti primul numar, a")
    a = input()
    print("Numarul introdus a=", a)
    print("Introduceti al 2-lea numar, b")
    b = input()
    print("Numarul introdus b=", b)
    print("a+b = ", int(a) - int(b))


def inmultirenumere():
    print('Introduceti primul numar, a')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al 2-lea numar, ')
    b = input()
    print('Numarul introdus b=', b)
    print('a*b = ', int(a)*int(b))


def impartirenumere():
    print('Introduceti primul numar, a')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al 2-lea numar, ')
    b = input()
    print('Numarul introdus b=', b)
    print('a/b = ', int(a)/int(b))


def arietriunghidr():
    print('Introduceti prima cateta, ab')
    ab = input()
    print('ab=', ab)
    print('Introduceti a 2-a cateta, ac')
    ac = input()
    print('ac=', ac)
    print('aria = (c1*c2) / 2, int(a)/int(b)/2')


def perimetrul():
    print('Introduceti prima latura, ab')
    ab = input()
    print('1-Latura introdusa a fost', ab)
    print('Introduceti a 2-a latura, bc')
    bc = input()
    print('2-Latura introdusa a fost', bc)
    print('Introduceti a 3-a latura, ac')
    ac = input()
    print('1-Latura introdusa a fost', ac)
    print('Perimetrul laturilor ab, bc, ac este ab + bc+ ac', ab+bc+ac)


if __name__ == '__main__':
    sumanumere()
    scaderenumere()
    inmultirenumere()
    impartirenumere()
    arietriunghidr()
    perimetrul()
