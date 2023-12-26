import os

restaurantes = [{"nome": "Praca XV", "categoria": "Japonesa", "ativo": False}, 
                {"nome": "Pizza Suprema", "categoria": "Italiana", "ativo": True},
                {"nome": "McDonalds", "categoria": "Fast Food", "ativo": True}]

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa '''
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      """)

def exibir_opcoes():
    ''' Exibe as opções disponíveis para escolha no menu do programa '''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar/Desativar restaurante")
    print("4. Sair\n")

def inicializa_tela(titulo):
    ''' Limpa a tela e inicializa mostrando o titulo da tela a ser aberta '''
    os.system("cls")
    linha = '*' * (len(titulo))
    print(linha)
    print(titulo)
    print(linha)
    print()

def finalizar_app():
    ''' finaliza o aplicativo chamando a função de inicializar tela com o titulo relacionado '''
    inicializa_tela("Finalizando o app")

def voltar_ao_menu_principal():
    ''' aguarda o usuário pressionar Enter para voltar ao menu principal '''
    input("Digite Enter para voltar ao menu principal")
    main()

def opcao_invalida():
    ''' responde ao usuário que a opção que ele escolheu no menu é inválida '''
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes 
    
    '''
    inicializa_tela("Cadastro de novo restaurante")
    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")

    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Essa função é responsável por listar os restaurantes cadastrados '''
    inicializa_tela("Listagem de restaurantes")

    print(f"{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | Status")
    print(f"{"-------------------".ljust(20)} | {"---------".ljust(20)} | ------")
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativado = "Ativado" if restaurante['ativo'] else 'Desativado'
        print(f"{nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativado}")

    print("")
    voltar_ao_menu_principal()

def ativar_restaurante():    
    ''' Essa função é responsável por ativar ou desativar um restaurante dependendo do seu status atual '''
    inicializa_tela("Ativar/Desativar restaurante")

    nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso.'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f"O restaurante {nome_do_restaurante} não foi encontrado.")

    print("")
    voltar_ao_menu_principal()

def escolher_opcoes():
    ''' Exibe opções do menu ao usuário e aguarda que ele escolha uma delas '''
    opcao_escolhida = input("Escolha uma opção: ")
    print(f"Você escolheu a opção {opcao_escolhida}.")

    try:
        opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal do programa '''
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()
