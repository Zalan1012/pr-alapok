#Adatbekérés while-ciklussal (szám bekérése megadott intervallumban)

szam = int(input('Adj meg egy számot 5 és 10 között! pl. 5,6,7,8,9,10 : '))

# while szam < 5 or 10 < szam:
while not 5 <= szam <= 10:
      szam = int(input('Helytelen érték! Adj meg egy számot 5 és 10 között! '))
print('Rendben!')
