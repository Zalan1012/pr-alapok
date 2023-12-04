# feladat_024
# A sztringek elemeire is így hivatkozhatunk

szo = "almafa"
print(szo[:3])

''' Üres lista és üres változó deklarálása
 A megadott szavakat fűzi a listához mindaddig, amíg a felhasználó csak egy ENTER-t nem nyom, azaz nem ad meg újabb értéket.
'''

  # üres listát hoz létre
gyumolcsok = []
  
  # kezdőérték nélküli változót hoz létre
gyumolcs = None
while gyumolcs != '':
    gyumolcs = input(f'Adj meg egy gyümölcsöt! ')
    if gyumolcs != '':
      # hozzáfűzi a listahoz
      gyumolcsok.append(gyumolcs)
print(gyumolcsok)