import os

restaurantes = [{'nome':'Pizza Hut', 'categoria':'Pizzaria', 'ativo':True},
                {'nome':'Burger King', 'categoria':'Fast Food', 'ativo':True},
                {'nome':'McDonalds', 'categoria':'Fast Food', 'ativo':False},
                {'nome':'Outback', 'categoria':'Restaurante', 'ativo':True}
]

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
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            definir_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def voltar_menu_principal():
    input('\nPressione qualquer tecla para voltar ao menu principal... ')
    main()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * len(subtitulo)
    print(linha)
    print(subtitulo)
    print(linha)
    print()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()
        
def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo...')
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    
    dados_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }
    
    restaurantes.append(dados_restaurante)
    
    print(f'\nO restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')
    
    print(f'{'Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    print()
                      
    for restaurante in restaurantes:
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {'Ativado' if restaurante['ativo'] else 'Desativado'}')
    
    voltar_menu_principal()
    
def definir_estado_restaurante():
    exibir_subtitulo('Definir estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja definir o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante['ativo'] = not restaurante['ativo']
            restaurante_encontrado = True
            estado_definido = 'Ativo' if restaurante['ativo'] else 'Inativo'
            print(f'O estado do restaurante "{nome_restaurante}" foi alterado com sucesso para {estado_definido}!')
            break
    if not restaurante_encontrado:
        print(f'O restaurante "{nome_restaurante}" não foi encontrado!')
        
    voltar_menu_principal()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
