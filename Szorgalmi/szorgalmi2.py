# Szám bekérése a felhasználótól
szam = float(input("Kérem, adjon meg egy számot: "))

# Szám értékelése
if szam > 0:
    print("A megadott szám pozitív.")
elif szam < 0:
    print("A megadott szám negatív.")
else:
    print("A megadott szám nulla.")
