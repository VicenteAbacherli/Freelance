x = float(input("Digite a coordenada x:"))
y = float(input("Digite a coordenada y:"))

def mostrar_quadrante ():

    if x > 0 and y > 0:
        print("O ponto está no primeiro quadrante")
    elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante.")
    elif x < 0 and y < 0:
        print("O ponto está no terceiro quadrante.")
    elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante.")
    else:
        print("O ponto está sobre um eixo ou na origem.")