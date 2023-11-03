# feladat_pelda
# be: szam
# ki: szám negatív

def beker_egy_szamot():
    szam = int(input('kérek egy számot:'))
    print(szam)

def beker_egy_szamot1(parameter1):
    szam1 = int(input('kérek egy számot:')) #50
    szam1 = szam1 + parameter1
    print(szam1)

def szamok_osszege():
    return 15+9


beker_egy_szamot()
beker_egy_szamot()
beker_egy_szamot1(100) #150
osszeg= szamok_osszege()
print(osszeg)
szamok_osszege()
    
"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
        print(f'A megadott szám {szam} negatív.')
print(f'>> A program vége! <<')
"""

# be: szam
# ki: szám negatív vagy nemnegatív
"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
      print(f'A megadott szám {szam} negatív.')
else:
      print(f'A megadott szám nemnegatív.')
print('>> A program vége! <<')
"""

# be: szam
# ki: szám negatív vagy a szám pozitív vagy a szám 0
"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print(f'A megadott szám {szam} negatív.')
elif szam == 0:
    print(f'A megadott szám {szam} nulla.')
else:
    print(f'A megadott szám {szam} pozitív.')
print('>> A program vége! <<')
"""
"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print(f'A megadott szám {szam} negatív.')
elif szam > 0:
    print(f'A megadott szám {szam} pozitív.')
elif szam == 0:
    print(f'A megadott szám {szam} nulla.')
print(f'>> A program vége! <<')
"""