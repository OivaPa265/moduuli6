
# määritää jos luvut listassa ovat parillisa
def list(numerot):
    #lisää parittomat tähän
    pariton =[]
    # katsoo jos listan luvut ovat parillisia
    for i in numerot:
        if i % 2 != 0:
            #jos eivät ole lisää ne paritomiin
            pariton.append(i)
            # pyöritää udestaan
    return pariton
#lista numeroista
lista = [9, 25, 32, 40,5,24,9,91]
# tulos
tulos= list(lista)
# printaa normaalin listan
print(f"listan kaikki luvut ovat {lista}")
#printa parittomat listasta
print(f"parittomat luvut listasta ovat {tulos} ")