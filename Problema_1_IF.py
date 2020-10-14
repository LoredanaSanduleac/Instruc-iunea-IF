e1=int(input("nr. elev"))
e2=int(input("nr. elev"))
e3=int(input("nr. elev"))
p1=int(input("introduceti punctajul primului elev"))
p2=int(input("introduceti punctajul elevului al doilea"))
p3=int(input("introduceti punctajul elevului al treilea"))
if ((p1>p2)and(p1>p3)):
    print("elevul cu nr",e1, "are cel mai mare punctaj")
if ((p2>p1)and(p2>p3)):
    print("elevul cu nr",e2, "are cel mai mare punctaj")
if ((p3>p1)and(p3>p2)):
    print("elevul cu nr",e3, "are cel mai mare punctaj")