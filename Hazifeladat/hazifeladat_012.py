import random

def penzfeldobas():
    felhasznalo_valasztas = input("Válassz fejet (F) vagy írást (Í): ").upper()
    if felhasznalo_valasztas not in ['F', 'Í']:
        print("Hibás választás. Csak fej (F) vagy írás (Í) választható.")
    pénzoldalak = ['F', 'Í']
    gep_valasztas = random.choice(pénzoldalak)
    print(f"A gép választása: {gep_valasztas}")
    if felhasznalo_valasztas == gep_valasztas:
        print("Gratulálok, eltaláltad!")
    else:
        print("Sajnálom, nem találtad el.")
penzfeldobas()
