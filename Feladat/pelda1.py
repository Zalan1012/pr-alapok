def menut_kiir(tipus):

    """
    A menü megjelenítése a képernyőn
    """

    if tipus == 2:
        print("1. Új adat bevitele")
        print("2. Kilépés a programból")
    elif tipus == 3:
        print("1. Új adat bevitele")
        print("2. Adatok módosítása / törlése")
        print("3. Kilépés a programból")
    else:
        print(f"A megadott menü tipusa {tipus} nem megfelelő")


tipus = int(input("Kérem, adja meg a menü számát: "))

menut_kiir(tipus)