import os

restaurantes = []

def exibir_nome_programa():
    print('''

███████╗ █████╗ ██████╗  ██████╗ ██████╗     ███████╗██╗  ██╗██████╗ ██████╗ ███████╗███████╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
███████╗███████║██████╔╝██║   ██║██████╔╝    █████╗   ╚███╔╝ ██████╔╝██████╔╝█████╗  ███████╗███████╗
╚════██║██╔══██║██╔══██╗██║   ██║██╔══██╗    ██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║
███████║██║  ██║██████╔╝╚██████╔╝██║  ██║    ███████╗██╔╝ ██╗██║     ██║  ██║███████╗███████║███████║
╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝

''')

def exibir_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
            
def opcao_invalida():
    print('Opção inválida!\n')
    input('Pressione qualquer tecla para voltar ao menu principal...')
    main()
        
def finalizar_app():
    os.system('cls')
    print('Finalizando o aplicativo...\n')
    
def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'\nO restaurante "{nome_do_restaurante}" cadastrado com sucesso!\n')
    input('Pressione qualquer tecla para voltar ao menu principal...')
    main()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
