'''1. Osztály létrehozása:'''
class Etel:
    def __init__(self,nev:str="",ar:int=1000):
        '''
        konstruktor feladata, hogy létrehozza a konkrét példányt
        a konkrét adatokkal a tervrajzból
        beállítsa az adattagokat - objektum tulajdonságok értékei
        '''
        self.nev=nev
        self.ar=ar
        self.allapot="Folyamatban"

    def keszul(self):
        self.allapot="Kész"

    def __str__(self):
        return(f"Étel neve: {self.nev}, Ár: {self.ar} Ft, Állapot: {self.allapot}")
