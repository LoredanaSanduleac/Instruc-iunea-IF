#Să se verifice dacă o literă introdusă este vocală sau consoană.
l=str(input("introduceti o litera"))
if ((l=="o")or(l=="u")or(l=="a")or(l=="e")or(l=="i")or(l=="ă")or(l=="î")or(l=="â")):
    print("litera",l,"este o vocală")
else:
    print("litera",l,"este o consoană")
