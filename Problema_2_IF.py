a=int(input("lungimea laturii 1 este: "))
b=int(input("lungimea laturii 2 este: "))
c=int(input("lungimea laturii 3 este: "))
if ((a<32000)and(b<32000)and(c<32000)):
    if((a<b+c)and(b<a+c)and(c<a+b)):
        print("DA")
    else:
        print("NU")