Nome = str(input("Digite o Nome: "))
Telefone = str(input("Digite o Telefone: "))
file = str

f = open("ListaTelefonica.txt", "a")
f.write("Nome: %s - Telefone: %s\n"%(Nome, Telefone))
f.close

f = file("ListaTelefonica.txt")

print("\nLista Telefonica\n")

