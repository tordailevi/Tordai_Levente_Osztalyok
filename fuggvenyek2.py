def ossz_fizetes(lista):
        osszeg:int=0
        for i in range(0, len(lista), 1):
            osszeg += lista[i].fizetes
        return osszeg

def legidosebb(lista):
    legidosebb = 0
    for i in range(0, len(lista), 1):
        if (lista[i].kor > lista[legidosebb].kor):
            legidosebb=i
    return legidosebb

def beosztott_poz(lista):
    beosztottak_szama:int=0
    for i in range(1, len(lista), 1):
     if (lista[i].pozicio == "Beosztott"):
          beosztottak_szama += 1
    return beosztottak_szama

def legkisebb_fizetes(lista):
    min_index = 0
    for i in range(0, len(lista), 1):
        if (lista[i].fizetes < lista[min_index].fizetes):
            min_index=i
    return min_index