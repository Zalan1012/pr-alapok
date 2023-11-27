henrik_kosarazik = input("Jön Henrik ma kosarazni? (igen/nem): ").lower()
hanna_kosarazik = input("Jön Hanna ma kosarazni? (igen/nem): ").lower()
if henrik_kosarazik == "igen" and hanna_kosarazik == "igen":
    print("Mindketten jönnek kosarazni.")
elif henrik_kosarazik == "nem" and hanna_kosarazik == "nem":
    print("Egyikük sem jön kosarazni.")
else:
    print("Csak az egyikük jön kosarazni.")
