#Andrei primeşte într-o zi trei note, nu toate bune. Se hotărăşte ca, dacă ultima notă este cel puţin 8, să le spună părinţilor toate
#notele primite iar dacă este mai mică decât 8, să le comunice doar cea mai mare notă dintre primele două. Introduceţi notele
#luate şi afişaţi notele pe care le va comunica părinţilor.
n1=int(input("introduceti prima nota: "))
n2=int(input("introduceti a doua nota: "))
n3=int(input("introduceti a treia nota: "))
if ((n1>1)and(n1<10)and(n2>1)and(n2<10)and(n3>1)and(n3<10)):
    if (n3>=8):
        print(n1,n2,n3,sep=" , ")
    if (n3<8):
        if(n1>n2):
            print(n1)
        else:
            print(n2)
