import random
# katsoo heitot jä mööritää tahkot
def hetto(tahk):
    heitto = random.randint(1, tahk)
    return heitto
#pyytää määrää
Syote = int(input("anna maksimi"))
# heittojen määrät
nmr=1
#heiton tulos
tulos=0

# jos heitto ei ole annetu määrä tekee tämän
while tulos != Syote:
    tulos = hetto(Syote)
    print(f"heitosta{nmr} tuli {tulos}")
    # jos tulos ei ollut annetu määrä lisää heiton numeroa
    if tulos != Syote:
        nmr = nmr+1
# jso heitosta tuli annetu määrä pritnaa tämän
print(f"nopasta tuli maksimi{Syote} äskeisellä heitolla jee :)")
print(f"heittoja tarvitiin {nmr}")