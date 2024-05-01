def par_ou_impar():
    numero= int(input('Insira um número:'))
    if numero %2 == 0:
        print('par')
    else:
        print('impar')

def idade():
    idade =int(input('Qual sua idade?\n'))
    if 0 <= idade <= 12:
        print(f'{idade} criança')
    elif 13 <= idade <= 18:
        print(f'{idade} Adolescente')
    else:
        print(f'{idade} acima de 18 anos')

idade()