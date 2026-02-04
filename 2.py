import random
# katsoo heitot jä mööritää tahkot
def hetto(tahk):
    heitto = random.randint(1, tahk)
    return heitto
# pyytää määrää
Syote = int(input("anna maksimi"))
# heiton tulos
tulos = 0
# jos heitto ei ole annetu määrä tekee tämän
while tulos != Syote:
    tulos = hetto(Syote)
    print(f"heitosta tuli {tulos}")
    if tulos == Syote:
     print(f"nopasta tuli maksimi{Syote} äskeisellä heitolla jee :)")
