import random
gondolt_szam = random.randint(1, 5)
felhasznalo_szam = int(input("Kérem, adjon meg egy számot 1 és 5 között: "))
if felhasznalo_szam == gondolt_szam:
    print("Gratulálok, eltaláltad!")
elif felhasznalo_szam < gondolt_szam:
    print("A gondolt szám nagyobb.")
else:
    print("A gondolt szám kisebb.")
