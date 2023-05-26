#Atividade 04 de 04 do Trabalho
#Inicio das Variáveis Globais
lista_peca = [] #lista vazia para armazenar as peças cadastradas
codigo_peca = 000

#Função para cadastrar peças
def cadastrarPeca(codigo):
    print('Bem-vindo ao menu de Cadastrar Peças')
    print('Código da Peça {:03d}' .format(codigo))
    nome = input('Entre com o nome da peça: ')
    fabricante = input('Entre com o fabricante da peça: ')
    valor = float(input('Entre com o valor(R$) da peça: '))
    #Criando um dicionario para armazenar as informações das peças
    dicionario_peca = {'codigo'     : codigo,
                       'nome'       : nome,
                       'fabricante' : fabricante,
                       'valor'      : valor}
    lista_peca.append(dicionario_peca.copy())
    print('')


#Função para Consultar peças
def consultarPeca():
    print('Bem-vindo ao menu de Consultar Peças')
    while True:
        opcao_menu_consultar = input('Escolha a opção desejada:\n' +
                                    '1-Consultar Todas Peças\n' +
                                    '2-Consultar Peça por Código\n' +
                                    '3-Consultar Peça por Fabricante\n' +
                                    '4-Retornar\n' +
                                    '>>>')
        if opcao_menu_consultar == '1':
            print('') #espaço em branco(pular linha) para ficar mais legivel
            print('CONSULTA TODAS AS PEÇAS')
            print('-------------------------')
            #Percorre todas as peças cadastradas na lista
            for peca in lista_peca:
                for key, value in peca.items():
                    print('{}: {}' .format(key,value))
                print('-------------------------')

        elif opcao_menu_consultar == '2':
            print('')
            print("CONSULTA POR CÓDIGO")
            peca_desejada = int(input('Entre com o código da Peça: '))
            print('-------------------------')
            for peca in lista_peca:
                if peca['codigo'] == peca_desejada: #Verifica se o código digitado é igual ao código do dicionario
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))
                    print('-------------------------')

        elif opcao_menu_consultar == '3':
            print('')
            print('CONSULTA POR FABRICANTE')
            peca_desejada = input('Entre com o fabricante da Peça: ')
            print('-------------------------')
            for peca in lista_peca:
                if peca['fabricante'] == peca_desejada: #Verifica se o fabricante digitado é igual ao fabricante do dicionario
                    for key, value in peca.items():
                        print('{}: {}'.format(key, value))
                    print('-------------------------')

        elif opcao_menu_consultar == '4':
            return # Sai da função consultarPeca e retorna para o programa principal

        else:
            # Caso o usuario digite uma opção invalida, solicita novamente a opção
            print('Você digitou uma opção inválida!\n' +
                  'Digite uma opção novamente')
            continue

#Função para remover peças
def removerPeca():
    print('Bem-vindo ao menu de Remover Peças')
    peca_desejada = int(input('Entre com o código da Peça que deseja remover: '))
    for peca in lista_peca:
        if peca['codigo'] == peca_desejada:  # o valor do campo código é igual ao código do dicionario
            lista_peca.remove(peca)
            print('Peça Removida')

#Inicio do Main
print('Bem Vindo a Loja de Peças do Marlos Augusto da Costa!')
while True:
    opcao_menu_principal = input('Escolha a opção desejada:\n' +
                                 '1-Cadastrar Peças\n' +
                                 '2-Consultar Peças\n' +
                                 '3-Remover Peças\n' +
                                 '4-Sair\n' +
                                 '>>>')
    if opcao_menu_principal == '1':
        print('')  # espaço em branco(pular linha) para ficar mais legivel
        codigo_peca = codigo_peca + 1 #contador para gerar codigos para cada peça
        cadastrarPeca(codigo_peca)

    elif opcao_menu_principal == '2':
        print('')
        consultarPeca()

    elif opcao_menu_principal == '3':
        print('')
        removerPeca()

    elif opcao_menu_principal == '4':
        print('Programa finalizado\n' +
              'Volte Sempre!')
        break #encerra o laço e encerra o programa

    else:
        #Caso o usuario digite uma opção invalida, solicita novamente a opção
        print('Você digitou uma opção inválida!\n' +
              'Digite uma opção novamente')
        continue
