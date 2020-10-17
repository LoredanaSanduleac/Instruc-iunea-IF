#La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
#secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi?
x=(int(input("introduceti locul pe care la ocupat Ionel: ")))
if ((x>=1)and(x<=100)):
    if ((x>=1)and(x<=25)):
        print("alba")
    if ((x>25)and(x<=50)):
        print("rosie")
    if ((x>50)and(x<=75)):
        print("albastra")
    if ((x>75)and(x<=100)):
        print("neagra")