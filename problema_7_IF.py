#Se consideră trei numere întregi. Dacă toate sunt pozitive, să se afişeze numărul mai mare dintre al doilea şi al treilea număr, în
#caz contrar să se calculeze suma primelor două numere.
n1=int(input("introduceti nr 1: "))
n2=int(input("introduceti nr 2: "))
n3=int(input("introduceti nr 3: "))
if ((n1>0)and(n2>0)and(n3>0)):
    if (n2>n3):
        print(n2)
    else:
        print(n3)
else: 
    print(n1+n2)