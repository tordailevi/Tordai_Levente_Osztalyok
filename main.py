import fuggvenyek
import fuggvenyek2
'''
Hozz létre egy osztályzatok listát és
osztalyzatok_lista=[3, 4, 5, 2, 3, 4, 5, 4]
nevek=["Béla", "Jenő", "Ági", "Rozi"]

nevek és nevekhez tartozó osztályzatok összetartoznak

etelek=["húsleves", "krumplis"]
ar=[1234,3456]

Új adatszerkezet - ami egybe tudja kezelni az összetartozó adatokat

szemely= {név: "Béla", osztalyzat:3}

kaja1= {nev:"húsleves", ar:1234}
kaja2= {nev:"krumplis", ar:2345}

objektumok - tulajdonságokkal (főnevek) és viselkedéssel (cselekvés) bíró adatszerkezet

Készítünk egy sablont, ami alapján le tudjuk gyártani a konkrét egyedeket.
OSZTÁLY - sablon - osztály - tervrajz
OBJEKTUM - konkrét egyedek - objektumok - konkrét termék
'''

from Etel import Etel

'''2. Létrehozzuk a konkrét példányt a tervrajz alapján:'''
#etel_lista=[]
#etel_lista.append(Etel("húsleves", 1234))
#etel_lista.append(Etel("krumplis", 2345))
#etel_lista.append(Etel("rántott hús",2145))
#etel_lista.append(Etel("palacsinta",1450))

#print("Szia! Én vagyok a " + etel_lista[0].nev + " Az állapotom: "+ etel_lista[0].allapot)

#etel_lista[0].keszul()

'''print("Szia! Én vagyok a " + etel_lista[0].nev + " Az állapotom: "+ etel_lista[0])
print("Szia! Én vagyok a " + etel_lista[1] + " Az állapotom: "+ etel_lista[1].allapot)'''

'''Írj metódust, amely paraméterében megkapja a listát és kiírja a z ételek neveit és árait!'''
#fuggvenyek.etlap(etel_lista)

'''Írj metódust, amely paraméterében megkapja a listát és megmondja az ételek átlag árát!'''
#osszeg=fuggvenyek.atlag_ar(etel_lista)
#print(f"Az ételek átlagára: {osszeg}")

'''Írj metódust, amely paraméterében megkapja a listát és megmondja a legdrágább étel nevét!'''
#max_index=fuggvenyek.legdragabb(etel_lista)
#print(f"A legdrágább étel neve és ára: {etel_lista[max_index].nev}, {etel_lista[max_index].ar}")

'''Hozz létre egy alkalmazott osztályt, amelyikben az alábbi infokat tudod tárolni egy cég dolgozóiról:
nev
szul_datum
fizetés
pozicio

Készíts hozzá egy kor metódust, ami megmondja az adott ember korát'''
#kor=Alkalmazott.kor()
#print({kor})
'''
Hozz létre legalább 5 embert, tedd bele őket listába.'''
from Alkalmazott import Alkalmazott
alkalmazott_lista=[]
alkalmazott_lista.append(Alkalmazott("Levente", 2003, 999999, "Boss"))
alkalmazott_lista.append(Alkalmazott("Milán", 2003, 750000, "Gyapotszedő"))
alkalmazott_lista.append(Alkalmazott("Tamás", 2006, 489000, "Beosztott"))
alkalmazott_lista.append(Alkalmazott("Bence", 2001, 624103, "Beosztott"))
alkalmazott_lista.append(Alkalmazott("Gergő", 2009, 546282, "Gyakornok"))

'''
-Mennyi az össz fizetés?'''
osszeg=fuggvenyek2.ossz_fizetes(alkalmazott_lista)
print(f"A fizetések összege: {osszeg}.")
'''-Hány éves a legidősebb ember?'''
legidosebb=fuggvenyek2.legidosebb(alkalmazott_lista)
print(f"A legidősebb ember: {legidosebb}.")
'''-Hány ember van "beosztott" pozicióban?'''
beosztottak_szama=fuggvenyek2.beosztott_poz(alkalmazott_lista)
print(f"Beosztott pozícióban lévők száma: {beosztottak_szama}")
'''-Kinek a legalacsonyabb a fizetése?'''
min_index=fuggvenyek2.legkisebb_fizetes(alkalmazott_lista)
print(f"A legkisebb fizetés: {min_index}")
'''++ Az osztálynak legyen egy fizetésemelés metódusa, amelyik a fizetést megemeli a 
paraméterében megadott százalék értékkel. A legkisebb fizetésű ember fizetését emeld meg 20%-kal.'''



