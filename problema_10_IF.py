#La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
#fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
#afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
#numărul de boabe de porumb.
ng=int(input("introduceti nr gaini: "))
nb=int(input("introduceti nr boabe: "))
i=nb//ng
#i-numarul de boabe pe care il primeste fiecare gaina
l=nb%ng
#l-numarul de boabe pe care il primeste curcnul Clapon 
if (i>l):
    print ("fiecare gaina a primit cu", i-l ,"boabe mai mult decat curcanul Clapon")
if (l>i):
    print ("curcanul Clapon a primit cu", l-i ,"boabe mai mult decat fiecare gaina")
if (l==i):
    print (l,"egalitate")
