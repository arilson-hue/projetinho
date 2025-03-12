nomes = ["ana","pedro"]
print (f"lista original {nomes}")

for cont in range (2):
    novo_nome = input("digite um nome: ")
    nomes.append(novo_nome)

print (f"adicionando 2 nomes: {nomes}")

resp = "s"
while resp == "s":
    novo_nome = input(f"Digite mais um nome: ")
    nomes.append(novo_nome)
    resp = input(f"cadastrar novo nome[s/n]: ")

print (f"adicionando n nomes: {nomes}")

nome_pesquisado = input("digite um nome para verificar: ")
if nome_pesquisado in nomes:
    print ("nome cadastrado")
else:
    print("nome nao cadastrado")
