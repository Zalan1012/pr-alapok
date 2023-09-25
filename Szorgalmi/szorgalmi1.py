# Életkor bekérése a felhasználótól
eletkor = int(input("Kérem, adja meg az életkorát: "))

# Életkor kategória megállapítása
if eletkor < 0:
    kategoria = "Hibás adat"
elif eletkor < 3:
    kategoria = "Csecsemő"
elif eletkor < 13:
    kategoria = "Gyerek"
elif eletkor < 20:
    kategoria = "Tinédzser"
elif eletkor < 65:
    kategoria = "Felnőtt"
else:
    kategoria = "Idős"

# Kategória kiírása
print(f"Az ön életkora a következő kategóriába tartozik: {kategoria}")
