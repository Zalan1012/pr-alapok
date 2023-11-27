import random
tipp = int(input(f"Kérek egy tippet (1,2,3):"))
generalt_szam = random.randint(1,3)
if tipp == generalt_szam:
    print(f"A tipped helyes! {tipp} {generalt_szam} ")
else:
    print(f"Rosszul tppeltél! {tipp} {generalt_szam}")