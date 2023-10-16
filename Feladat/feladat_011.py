# feladat_011

"""
kérjünk be két egész számot, szám1 ás szám2.
Hasonlítsuk össze a két számot, és írassuk ki, hogy a szám1
kisebb mint a szám 2,
vagy a szám2 kisebb mint a szám1
vagy a szám1 egyenlő a szám2-vel
"""

szám1 = input("írj egy számot:")
szám2 = input("írj mégegy számot:")
szám1 = int(szám1)
szám2 = int(szám2)

#------------------------------------------------------------

"""
if szám1 < szám2:
    print(f"A szám1 kisebb mint a szám2")
elif szám2 < szám1:
    print(f"A szám2 kisebb mint a szám1")
else:
    print("A szám1 egyenlő a szám2-vel")
"""

#------------------------------------------------------------

"""
if szám1 < szám2:
    print(f"A szám1 kisebb mint a szám2")
if szám2 < szám1:
    print(f"A szám2 kisebb mint a szám1")
if szám1 == szám2:
    print("A szám1 egyenlő a szám2-vel")
"""

#-----------------------------------------------------------

if szám1 < szám2:
    print(f"A szám1 kisebb mint a szám2")
elif szám2 < szám1:
    print(f"A szám2 kisebb mint a szám1")
elif szám1 == szám2:
    print(f"A szám1 egyenlő a szám2-vel")