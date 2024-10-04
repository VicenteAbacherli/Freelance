
import os


def exibir_nome_do_programa():
    print('Restaurantes\n')


def exibir_opcoes():

    print('1.Cadastrar restaurante')
    print('2.Listar restaurante')
    print('3.Ativar restaurante')
    print('4.Sair\n')


def finalizar_app():
    os.system('cls')
    print('Finalizando app!\n')


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção:'))
    # definindo a função pra fechar o aplicativo

    if opcao_escolhida == 1:
        print('Restaurante cadastrador')
    elif opcao_escolhida == 2:
        print('Lista de restaurantes')
    elif opcao_escolhida == 3:
        print('Restaurante ativado')
    else:
        finalizar_app()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()

