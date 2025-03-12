cores = ("azul","vermelho", "rosa","roxo","laranja")
print(cores)

qtd =len(cores)

print(f"tenho {qtd} opçoes de cores")

cor =input ("digite uma cor: ")
qtd = cores.count(cor)

print(f"temos {qtd} tipo de {cor}")

if cor in cores:
    qtd = cores.count
    print (f"a cor {cor} existe na loja")
else:
    print (f"a cor {cor} nao existe na loja")

aluno = ("arilson", 10,  8)
nome, nota1, nota2 = aluno
media = (nota1 + nota2) / 2
print(f"o aluno {nome} com as notas {nota1} e {nota2} tem media {media}")