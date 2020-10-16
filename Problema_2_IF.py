#La ora de matematică Gigel este scos la tablă. Profesoara îi dictează trei numere şi îi cere să verifice dacă cele trei numere pot fi
#laturile unui triunghi. Ajutaţi-l pe Gigel să afle rezultatul. Scrieţi un program care primeşte numerele lui Gigel, care sunt mai mici
#ca 32000, şi returnează DA sau NU. Observaţie: Trei numere pot fi laturile unui triunghi numai dacă fiecare este mai mic ca
#suma celorlalte două.
a=int(input("lungimea laturii 1 este: "))
b=int(input("lungimea laturii 2 este: "))
c=int(input("lungimea laturii 3 este: "))
if ((a<32000)and(b<32000)and(c<32000)):
    if((a<b+c)and(b<a+c)and(c<a+b)):
        print("DA")
    else:
        print("NU")
