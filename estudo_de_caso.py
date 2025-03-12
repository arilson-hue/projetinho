banco_dados = []


def selecionar_menu(opcao):
    if (opcao == '1'):
        print('----->adicionando estoque<-----')

        novo = input('Digite o nome do novo produto no estoque: ')
        preco = float(input('Digite o preço do item: '))
        qtd = int(input('Digite a quantidade: '))

        novo_produto = {
            'nome do produto': novo,
            'preco': preco,
            'qtd': qtd
        }


        banco_dados.append(novo_produto)
        print(f"Produto '{novo}' adicionado com sucesso!")
    elif (opcao == '2'):
        print('----->visualuzando estoque<-----')
        if not banco_dados:
            print("Nenhum produto novo cadastrado no estoque!")
        else:
            for i, produto in enumerate(banco_dados, start=1):
                print(f"Produto {i}: Nome: {produto['nome do produto']}, Preço: {produto['preco']}, Quantidade: {produto['qtd']}")
        
    elif (opcao == '3'):
        print('----->atualizando estoque<-----')

        nome_produto = input('Digite o nome do produto que deseja atualizar: ')
        produto_encontrado = None

        for produto in banco_dados:
            if produto['nome do produto'] == nome_produto:
                produto_encontrado = produto
                break

        if produto_encontrado:
            print(f"Produto encontrado: Nome: {produto_encontrado['nome do produto']}, Preço: {produto_encontrado['preco']}, Quantidade: {produto_encontrado['qtd']}")
            novo_nome = input('Digite o novo nome do produto (ou pressione Enter para manter): ')
            novo_preco = input('Digite o novo preço do produto (ou pressione Enter para manter): ')
            nova_qtd = input('Digite a nova quantidade do produto (ou pressione Enter para manter): ')

            if novo_nome:
                produto_encontrado['nome do produto'] = novo_nome
            if novo_preco:
                produto_encontrado['preco'] = float(novo_preco)
            if nova_qtd:
                produto_encontrado['qtd'] = int(nova_qtd)

            print('Produto atualizado com sucesso!')
        else:
            print('Produto não encontrado!')
        print('atualizando produto...')
    elif (opcao == '4'):
        print('excluindo produto...')
        nome_produto = input('Digite o nome do produto que deseja excluir: ')
        produto_encontrado = None

        for produto in banco_dados:
            if produto['nome do produto'] == nome_produto:
                produto_encontrado = produto
                break

        if produto_encontrado:
            banco_dados.remove(produto_encontrado)
            print(f"Produto '{nome_produto}' excluído com sucesso!")
        else:
            print('Produto não encontrado!')
    elif (opcao == '5'):
        print('saindo do sistema...')
        return False
    else: 
        print('opcao incorreta, tente novamente')
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