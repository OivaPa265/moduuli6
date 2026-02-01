#määritää laskumuutoksen
def oljy(gal):
    Lit = gal *3.785
    return Lit
#katsoo jos annetu numero ei ole negatiivinen
while True:
    #pyytää syoteen
     syote = int(input("paljonko oljyä"))

    # kutsuu def:in
     mar=oljy(syote)
    # katsoo jos annetu luku ei ole negatiivinen
     if syote>0:
      print(f"{syote}gal = {mar}L")
    # jos annetu luku on negatiivinen printaa tämän
     else:
         print("annoit negatiivisen luvun ohjelma piti lopettaa :(")
         break





