class Alkalmazott:
    def __init__(self, nev:str="", szul_datum:int=0, fizetes:int=0, pozicio:str=""):
        self.nev=nev
        self.szul_datum=szul_datum
        self.fizetes=fizetes
        self.pozicio=pozicio
        self.kor_b()

    def kor_b(self):
        self.kor:int= 2024 - self.szul_datum
   
    def __str__(self):
        return(f"Név: {self.nev}, Születési év: {self.szul_datum}, Fizetés: {self.fizetes}, Pozíció: {self.pozicio}")
