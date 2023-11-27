szam = int(input("Kérem, adjon meg egy egész számot: "))
if szam % 3 == 0 and szam % 4 == 0:
    print(f"A megadott szám ({szam}) 3-mal és 4-gyel is osztható.")
elif szam % 3 == 0:
    print(f"A megadott szám ({szam}) csak 3-mal osztható.")
elif szam % 4 == 0:
    print(f"A megadott szám ({szam}) csak 4-gyel osztható.")
else:
    print(f"A megadott szám ({szam}) sem 3-mal, sem 4-gyel nem osztható.")
