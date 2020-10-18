#Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?
n=(int(input("Ionel este nr: ")))
if n<=4:
    print("casuta nr 1")
else:
    print("casuta nr",(n//4)+1)