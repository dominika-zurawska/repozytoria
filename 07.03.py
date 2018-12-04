def f(x):	# funkcja f z tresci zadania
	return (x**3) + 2 * (x**2) - 4 * x - 10

def bisekcja(a, b, eps):	# a - poczatek przedzalu, b - koniec przedzialu, eps - dokladnosc
	""" Funkcja oblicza miejsce zerowe funkcji f na podanym przedziale [a,b] z dokladnoscia eps """
	x1 = (a+b)/2.0	# strzelamy w srodek
	if f(x1) == 0:	# trafilismy miejsce zerowe
		return x1
	elif (b-a) < eps:	# skonczyla sie dokladnosc
		return x1
	else:
		
		if f(x1) * f(a) < 0:
			b = x1	# bierzemy lewy przedzial
		else:
			a = x1	# bierzemy prawy przedzial

		return bisekcja(a,b,eps)	# wywolaj funkcje dla mniejszych argumentow

wynik = bisekcja(1.0, 3.0, 0.0001)
print("f(", wynik, ") = ", f(wynik))
