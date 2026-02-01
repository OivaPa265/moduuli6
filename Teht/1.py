import random
def heitot():
    #tekee satunaisen numeron yhden ja kuuden välillä
 heitto=random.randint(1,6)
    #aloitaa uuden heiton
 return heitto
#katsoo kuinka monta heittoa on tehty
nmr=1
#näyttää nopanheiton tuloksen
tulo=0
# jos nopenheiton tulos ei ole 6 aloita uudestaan ja printaa tuloksen
while tulo!=6:
   tulo = heitot()# muutaa satunaisen numerom printattavaksi luvuksi
   print(f"nopan {nmr} tulos oli {tulo} ")
   nmr=nmr+1# heittojen määrä
# jos tulos on 6 printaa tämän
if tulo==6:
    print(f"Äskeisestä heitosta tuli 6 jee :)")
