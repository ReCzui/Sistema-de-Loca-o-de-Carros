import os



def linha(tam=20):
    print('-=' * tam)


def menu():
    print(''' >>>>   \033[1mO que você deseja fazer\033[m:
        \033[34m[1]\033[m Mostrar Portfólio
        \033[34m[2]\033[m  Alugar um carro 
        \033[34m[3]\033[m  Devolver o carro
        \033[34m[4]\033[m  Encerrar programa ''')


def calcular_diaria(carro, dias):
    if carro in diária_carros:
        preço_diaria = diária_carros[carro]
        total = preço_diaria * dias
    print(f'O aluguel totalizará \033[1mR$ {total:.2f}\033[m.')



lista_carros = ['Chevrolet Tracker',
    'Chevrolet Onix',
    'Chevrolet Spin',
    'Hyundai HB20',
    'Hyundai Tucson',
    'Fiat Uno',
    'Fiat Mobi',
    'Fiat Pulse']

diária_carros = {'Chevrolet Tracker': 120,
    'Chevrolet Onix': 90,
    'Chevrolet Spin': 150,
    'Hyundai HB20': 85,
    'Hyundai Tucson': 120,
    'Fiat Uno': 60,
    'Fiat Mobi': 70,
    'Fiat Pulse': 130}

alugados = []



# PROGRAMA PRINCIPAL

linha()
print('  \033[36mBEM VINDO À LOCADORA DE CARROS\033[m  ')
linha()


while True:
    menu()
    opção = int(input('\n\033[1mEscolha uma das opções:\033[m '))
    linha()
    if opção == 4:
        print('\033[31mSistema encerrado! Muito Obrigada!\033[m')
        break
    elif opção == 1:
        n = 0
        for carros in lista_carros:
            print(f'\033[36m[{n}]\033[m {carros}')
            n = n + 1
    elif opção == 2:
        print('\033[1m\033[34m[ALUGAR]\033[m Dê uma olhada em nosso portifólio:\033[m')
        print()
        n = 0
        for k, v in diária_carros.items():
            print(f'\033[36m[{n}]\033[m {k}: \033[1mR$ {v:.2f} /dia\033[m')
            n = n + 1
        linha()
        escolher_carro = int(input('\n\033[1mEscolha o código do carro:\033[m '))

        qtd_dias = int(input('\033[1mEscolha por quantos dias desejar alugar o carro:\033[m '))
        print(f'Você escolheu \033[34m{lista_carros[escolher_carro]}\033[m por {qtd_dias} dias.')

        calcular_diaria(lista_carros[escolher_carro], qtd_dias)
        confirmação = int(input('Deseja confirmar o aluguel? \033[1m0 - SIM | 1 - NÃO\033[m '))
        linha()
        if confirmação == 0:
            alugado = lista_carros.pop(escolher_carro)
            alugados.append(alugado)
        else:
            continue
    elif opção == 3:
        print('\033[34mDEVOLVER CARRO\033[3m')
        if not alugados:
            print()
            print('\033[31mNenhum carro alugado atualmente!\033[m')
            linha()
            menu()
        else:
            print('\033[1mO seguintes carros estão alugados:\033[m')
            for carro in alugados:
                print(f'{alugados.index(carro)} - {carro}')

            devolver = int(input('\033[1mInsira o carro que deseja devolver:\033[m '))
            alugado2 = alugados.pop(devolver)
            lista_carros.append(alugado2)
            print('\033[34Carro devolvido com sucesso!\033[m')



