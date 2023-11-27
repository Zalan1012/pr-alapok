szam = int(input("Kérem, adjon meg egy egész számot: "))
if szam > 0 and szam % 2 == 0:
    print(f"A megadott szám ({szam}) pozitív páros.")
elif szam < 0 and szam % 2 != 0:
    print(f"A megadott szám ({szam}) negatív páratlan.")
else:
    print("A megadott szám nem felel meg a vizsgálati feltételeknek.")
