eventos = []  
inscricoes = []  


def selecionar_menu(opcao):
    if opcao == '1':
        print('-----> Cadastro de Eventos <-----')
        nome_evento = input('Digite o nome do evento: ')
        data = input('Digite a data do evento (DD/MM/AAAA): ')
        descricao = input('Digite uma breve descrição do evento: ')

        novo_evento = {
            'nome': nome_evento,
            'data': data,
            'descricao': descricao
        }

        eventos.append(novo_evento)
        print(f"Evento '{nome_evento}' cadastrado com sucesso!")

    elif opcao == '2':
        print('-----> Visualização de Eventos Disponíveis <-----')
        if not eventos:
            print("Nenhum evento disponível!")
        else:
            for i, evento in enumerate(eventos, start=1):
                print(f"Evento {i}: Nome: {evento['nome']}, Data: {evento['data']}, Descrição: {evento['descricao']}")

    elif opcao == '3':
        print('-----> Atualização de Evento <-----')
        nome_evento = input('Digite o nome do evento que deseja atualizar: ')
        evento_encontrado = None

        for evento in eventos:
            if evento['nome'] == nome_evento:
                evento_encontrado = evento
                break

        if evento_encontrado:
            print(f"Evento encontrado: Nome: {evento_encontrado['nome']}, Data: {evento_encontrado['data']}, Descrição: {evento_encontrado['descricao']}")
            novo_nome = input('Digite o novo nome do evento (ou pressione Enter para manter): ')
            nova_data = input('Digite a nova data do evento (ou pressione Enter para manter): ')
            nova_descricao = input('Digite a nova descrição do evento (ou pressione Enter para manter): ')

            if novo_nome:
                evento_encontrado['nome'] = novo_nome
            if nova_data:
                evento_encontrado['data'] = nova_data
            if nova_descricao:
                evento_encontrado['descricao'] = nova_descricao

            print('Evento atualizado com sucesso!')
        else:
            print('Evento não encontrado!')

    elif opcao == '4':
        print('-----> Exclusão de Eventos <-----')
        nome_evento = input('Digite o nome do evento que deseja excluir: ')
        evento_encontrado = None

        for evento in eventos:
            if evento['nome'] == nome_evento:
                evento_encontrado = evento
                break

        if evento_encontrado:
            eventos.remove(evento_encontrado)
            print(f"Evento '{nome_evento}' excluído com sucesso!")
        else:
            print('Evento não encontrado!')

    elif opcao == '5':
        print('-----> Visualizar Inscrições <-----')
        if not inscricoes:
            print("Nenhuma inscrição registrada!")
        else:
            for i, inscricao in enumerate(inscricoes, start=1):
                print(f"Inscrição {i}: Nome: {inscricao['nome']}, Evento: {inscricao['evento']}")

    elif opcao == '6':
        print('-----> Inscrição em Eventos <-----')
        nome = input('Digite o nome do participante: ')
        nome_evento = input('Digite o nome do evento para inscrição: ')

        evento_encontrado = next((evento for evento in eventos if evento['nome'] == nome_evento), None)

        if evento_encontrado:
            inscricao = {
                'nome': nome,
                'evento': nome_evento
            }
            inscricoes.append(inscricao)
            print(f"{nome} inscrito no evento '{nome_evento}' com sucesso!")
        else:
            print(f"O evento '{nome_evento}' não foi encontrado.")

    elif opcao == '7':
        print('Saindo do sistema...')
        return False

    else:
        print('Opção incorreta, tente novamente')
    return True


def exibir_menu():
    while True:
        print('-----> MENU <-----')
        print('1 - Cadastro de Eventos')
        print('2 - Visualização de Eventos Disponíveis')
        print('3 - Atualização de Evento')
        print('4 - Exclusão de Eventos')
        print('5 - Visualizar Inscrições')
        print('6 - Inscrição em Eventos')
        print('7 - Sair do sistema')
        opcao = input('Selecione uma opção: ')
        if not selecionar_menu(opcao):
            break


exibir_menu()

