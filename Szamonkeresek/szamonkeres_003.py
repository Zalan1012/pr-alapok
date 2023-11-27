#Kakszi Zalán 10/B 6.
#A programm a pénzfelldobást modellezi. Kérdezze meg a felhasználótól a választását fej vagy írás majd adjon tájékoztatást hogy eltalálta e?
import random

def penzfeldobas():
    tipp = input("Válassz fejet (f) vagy írást (í): ").lower()
    if tipp != 'f' and tipp != 'í':
        print("Hibás választás. Kérlek válassz fejet (f) vagy írást (í).")
    eredmeny = random.choice(['fej', 'írás'])
    if tipp == eredmeny:
        print(f'Gratulálok! Eltaláltad, a válasz {eredmeny}.')
    else:
        print(f'Sajnálom, nem találtad el. A válasz {eredmeny}.')

penzfeldobas()
