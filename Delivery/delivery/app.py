
import os
'''Esse IMPORT importa uma biblioteca python'''

'''Isso é uma lista, como se fosse um banco de dados local alimentado manualmente ou quando roda o terminal.'''
restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]


def exibir_nome_do_programa():
    '''Essa função exibi o título do restaurante'''
    print('''░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  \n''')


def exibir_opcoes():
    '''Essa função exibi as opções de restaurantes'''
    print('1.Cadastrar restaurante')
    print('2.Listar restaurante')
    print('3.Alternar estado do restaurante')
    print('4.Sair\n')


def finalizar_app():
    '''Essa função finaliza o app'''
    exibir_subtitulo('Finalizando app ')


def voltar_ao_menu_principal():
    '''Essa função volta ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    '''Deixa pré setado oq sera feito caso use OPCAO_INVALIDA'''
    print('Opção inválida!')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''Essa função é utilizada para deixar programado oq a função EXIBIR_SUBTITULO ira fazer'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa função é usada para cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes ')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {
                      nome_do_restaurante}: ')
    dado_do_restaurante = {'nome': nome_do_restaurante,
                           'categoria': categoria, 'ativo': False}
    restaurantes.append(dado_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso! ')
    voltar_ao_menu_principal()


def listar_restaurantes():
    # Essa função exibi a pagina lista de restaurantes
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {
          'Catehoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)
                   } | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    # Essa função altera o status do restaurante de true pra false e vice e versa
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {
                nome_restaurante} foi desativado com sucesso'
            print(mensagem)
        if not restaurante_encontrado:
            print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    # Essas função armazena o numero da função escolhida que foi exibida no início
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        # definindo a função pra fechar o aplicativo

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    # A função main esta sendo utilizada para armazenar outras funções como: a de limpar a tela toda, exibir nome e etc.
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
