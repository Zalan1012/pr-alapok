#Kakszi Zalán 10/B
szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print(f'A megadott szám {szam} negatív.')
elif szam > 0:
    print(f'A megadott szám {szam} pozitív.')
elif szam == 0:
    print(f'A megadott szám {szam} nulla.')
print(f'>> A programmnak vége! <<')