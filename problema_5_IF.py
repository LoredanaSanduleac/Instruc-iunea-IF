#Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
#exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi.
zc=int(input("ziua curenta"))
lc=int(input("luna curenta"))
ac=int(input("anul curent"))
zn=int(input("ziua nasterii"))
ln=int(input("luna nasterii"))
an=int(input("anul nasterii"))
if ((zc<31)and(zn<31)and(lc<12)and(ln<12)):
    if ((zc>zn)and(lc>ln)):
        print(ac-an)
    else:
        print((ac-an)-1)
