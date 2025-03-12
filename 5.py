usuarios = {"ana","lucas","rodinei"}
usuarios.add ("felipe")
print(usuarios)

usuarios_digitados = input("digite seu usuario: ")

if usuarios_digitados in usuarios:
    print(f"usario cadastrado!")
else:
    print(f"usario nao cadastrado!")


usuarios_novos = {"ricardo","angela","reinier"}
todos_usuarios = usuarios.union(usuarios_novos)
print(todos_usuarios)
