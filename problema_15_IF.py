#Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În
#ce clasa va fi repartizat (A, B, C, D sau E)?
n=int(input("Radu e pe locul: "))
if ((n>=1)and(n<=125)):
    if ((n>=1)and(n<=25)):
        print("A")
    if ((n>25)and(n<=50)):
        print("B")
    if ((n>50)and(n<=75)):
        print("C")
    if ((n>75)and(n<=100)):
        print("D")
    if ((n>100)and(n<=125)):
        print("E")