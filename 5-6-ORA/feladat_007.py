# feladat:007
# dk9 109-oldal

""""
gondolt_szám := 4
ki: „gondoltam egy számra”
be: tipp
tipp átalakítása egésszé
elágazás
ha tipp = gondolt_szám:
ki: kétsoros dicséret
különbenha csak egyet 
tévedett:
ki: csak egyet tévedtél
különben:
ki: ugratás
elágazás vége
ki: búcsú
"""

gondolt_szám = 4
tipp = input('Gondoltam egy számra. Tippeld meg! ')
tipp = int(tipp)
if tipp == gondolt_szám:
    print(f'Ügyes!')
    print(f'Gratulálok.')
elif tipp == gondolt_szám + 1 or tipp == gondolt_szám - 1:
    print(f'Ó, csak eggyel tévedtél.')
else:
    print(f'Hosszan gondolkodtál rajta?:)')
    print(f'Nem érte meg.;)')
print('Pápá.')