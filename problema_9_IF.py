#Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
#câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
#numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor.
a1a=int(input("introduceti nr bilelor albe mici: "))
a1r=int(input("introduceti nr bilelor rosii mici: "))
a1v=int(input("introduceti nr bilelor verzi mici: "))
b1a=int(input("introduceti nr bilelor albe mari: "))
b1r=int(input("introduceti nr bilelor rosii mari: "))
b1v=int(input("introduceti nr bilelor verzi mari: "))
#a1-bile mici
#b1-bile mari
Mari=b1a+b1r+b1v
Mici=a1a+a1r+a1v
if Mari>Mici:
    print("sunt",Mari, "bile mari")
else:
    print("sunt",Mici, "bile mici")
a=a1a+b1a
r=a1r+b1r
v=a1v+b1v
if ((a>r)and(a>v)):
    print(a)
if ((r>a)and(r>v)):
    print(r)
if ((v>a)and(v>r)):
    print(v)