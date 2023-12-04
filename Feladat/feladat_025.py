# feladat_025
# Lista bejárása

tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']
szamlalo = 0
index = 0
for tantargy in tantargyak:
    print(f"A tantárgyak lista {index}. indexű eleme: {tantargy}")
    szamlalo = szamlalo + 1
    index = index + 1
print(f"{szamlalo} eleme van a tantárgyaknak")