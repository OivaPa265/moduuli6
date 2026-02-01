#määritää numerot
def nun(numerot):
    #tekee lasku muutoksen
    suma = 0
    for luku in numerot:
        #summan lasku muutos
        suma += luku
        # pyoritää numeto uudestaan kunnes valmis
    return suma
# annetut luvut
lista = [9, 25, 32, 40,5,24,9,91]
# katsoo tuloksen
tulos = nun(lista)
#printaa vastauksen
print(tulos)
