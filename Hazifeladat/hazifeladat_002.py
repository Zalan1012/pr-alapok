import math
sugar = float(input("Kérem, adja meg a kör sugarát: "))
kerulet = 2 * math.pi * sugar
terulet = math.pi * sugar**2
print(f"A kör kerülete: {kerulet:.2f}")
print(f"A kör területe: {terulet:.2f}")
