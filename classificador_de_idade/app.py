idade = int(input('Qual a sua idade?'))

if 0 < idade <= 12:
    print('Criança')

elif 12 < idade < 18:
    print('Adolecente')
elif idade >= 18:
    print('Adulto')
else:
    print('Valor inválido!') 

