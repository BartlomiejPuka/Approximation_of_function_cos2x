#@author: Bartłomiej Puka f(x) = cos(2x)
#  Projekt nr 1. Tablicowanie funkcji. (10pkt.)
# - Policz wartości funkcji $y = f(x)$ we wszystkich punktach podziału na $n$ części przedziału $[a, b]$.
# - Funkcja $f(x)$ dana jest w postaci rozwinięcia w szereg potęgowy i w postaci wzoru analitycznego.
# - Obliczanie sumy szeregu wykonaj z dokładnością $\epsilon$.
# - Algorytm obliczania sumy szeregu zapisz w oddzielnej funkcji.
# - Uzupełnij funkcję obliczającą sumę szeregu tak, by sumowanych było co najwyżej M wyrazów szeregu.
# Oznacza to, że przerwanie sumowania może nastąpić również wtedy, gdy nie została osiągnięta żądana dokładność.
# - Informacja o tym, czy została osiągnięta dokładność czy też nie winna być przekazana z funkcji obliczającej sumę szeregu.
# - Uzupełnij funkcję obliczającą sumę szeregu tak, by funkcja zwracała dodatkowo liczbę sumowanych wyrazów szeregu.

import math

def znak(i):
    k = int((i+1)/2)
    c = math.cos(k*math.pi)
    z = 0
    if i == 0:
        z = 1
    elif  c == 1:
        z = 1
    else:
        z = -1
    return z

def silnia(i):
    if i<2:
        return 1
    return i*silnia(i-1)

def fun(x,eps,a):
    s = math.cos(a)
    an = math.cos(a)
    n = 1
    while abs(an)>eps*abs(s):
        # print('a=',a,' eps=',eps)
        z = znak(n)
        if n % 2 == 0:
            wyraz = math.cos(a)
            #sinczycos = 'cos'
        if n % 2 == 1:
            wyraz = math.sin(a)
            #sinczycos = 'sin'
        #print('znak ='+str(z),'!n=!'+str(sil),' x^n='+str(math.pow(x,n)),'a='+str(t),'tryg='+sinczycos, sep=' | ')
        an = z*wyraz
        an = an * math.pow(x,n)
        an = an/silnia(n)
        s = s + an
        n = n + 1
        if n >= M and M >= 0:
            if abs(an)>eps*abs(s):
                print('* Nie została osiągnięta żądana dokładność eps dla zsumowanych wyrazów! *')
            print('* Zostało zsumowanych ',n,' wyrazow szeregu, z racji tego ze liczba M wynosi',M,' przerywamy sumowanie! *')
            break
        if abs(an)<eps*abs(s):
            print('* Żadana dokładność eps została osiągnięta przy zsumowaniu ',n,' wyrazów ! *')
            print('* Liczba zsumowanych wyrazów jest równa ',n,'! *')
    return s

if __name__ == '__main__':
    a = input('Podaj a: ')
    b = input('Podaj b: ')
    n = input('Podaj liczbę podziałów przedziału <a,b>: ')
    eps = input('Podaj tolerancję dla obliczeń: ')
    M = input('Podaj liczbe co najwyżej M sumowanych wyrazów szeregu: ')

    # tablicowanie
    a = float(a)
    b = float(b)
    n = int(n)
    M = int(M)
    eps = float(eps)
    dane = []
    if a >= b:
        print('Błąd danych')
        raise NotImplementedError
    dx = (b - a) / n  # krok z jakim tablicujemy funkcję
    x = a  # rozpoczynamy od początku przedziału
    print('|     x     |     f(x)      |     f_s(x)    |')
    while x <= b:  ## myslałem nad for range x in (x,b) ale x jest float
        y = fun(x, eps, a)  # wartość funkcji w punkcie z szeregu
        ys = math.cos(x + a)  # wartość ścisła funkcji w pukcie x
        print('|%11f|%15.6f|%15.6f|' % (x, y, ys))
        dane.append('|%11f|%15.6f|%15.6f|' % (x, y, ys))
        x = x + dx
    print('|||||||||||||||||||||||||||||||||||||||||||||')
    print('WYNIKI bez informacji o sum. wyrazach i dokł.')
    print('|     x     |     f(x)      |     f_s(x)    |')
    for x in dane:
        print(x)
