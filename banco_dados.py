banco_dados = []
estoque_atual = {'nome do produto': 'teclado', 'preco': '30 reais', 'qtd': '50'}

def selecionar_menu(opcao):
    if opcao == '1':
        # Adicionar novo produto
        novo = input('Digite o nome do novo produto no estoque: ')
        preco = float(input('Digite o preço do item: '))
        qtd = int(input('Digite a quantidade: '))

        novo_produto = {
            'nome do produto': novo,
            'preco': preco,
            'qtd': qtd
        }

        banco_dados.append(novo_produto)  # Adiciona apenas o dicionário
        print(f"Produto '{novo}' adicionado com sucesso!")
    elif opcao == '2':
        # Visualizar estoque
        print('-----> Visualizando estoque <-----')
        if not banco_dados:
            print("Nenhum produto cadastrado no estoque!")
        else:
            for i, produto in enumerate(banco_dados, start=1):
                print(f"Produto {i}: Nome: {produto['nome do produto']}, Preço: {produto['preco']}, Quantidade: {produto['qtd']}")
        print(estoque_atual)
    elif opcao == '3':
        print('Atualizando produto...')
        # Lógica para atualizar o produto
    elif opcao == '4':
        print('Excluindo produto...')
        # Lógica para excluir o produto
    elif opcao == '5':
        print('Saindo do sistema...')
        return False
    else:
        print('Opção incorreta, tente novamente')
    return True

def exibir_menu():
    while True:
        print('-----> MENU <-----')
        print('1 - Adicionar produto')
        print('2 - Visualizar estoque')
        print('3 - Atualizar produto')
        print('4 - Excluir produto')
        print('5 - Sair do sistema')
        opcao = input('Selecione uma opção: ')
        if not selecionar_menu(opcao):
            break

exibir_menu()