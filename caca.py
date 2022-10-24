def caca(cordenadas = False):
    from random import choice
    from Palavras import palavra
    W = None
    tipo = choice(['I','H','V'])
    NA = choice([1,2])
    '''IMPORTAÇÕES'''
    from random import choice
    '''VARIAVEIS'''
    linhas = 0
    recepto = ''
    caca_palavras = ''
    c = 0
    cont = 0
    palavra = palavra()
    palavracorreta = palavra
    if NA == 2:
        palavra = palavra[::-1]
    '''LISTAS'''
    lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
             'W', 'X', 'Y', 'Z']
    coluna = list(range(0, 19))
    escolhido = choice(coluna)
    posicao = list(range(0, 66, 2))
    # DETERMINA A PATE A QUAL A PALAVRA VAI FICA
    #HORIZONTAL
    if tipo == 'H':
        palavra = ' '.join(palavra)
        while True:
          posicao2 = choice(posicao)
          if 65 - posicao2 >= len(palavra):
              break
    #INCLINADO
    elif tipo == 'I':
        while True:
            escolhido = choice(coluna)
            if 18 - len(palavra) >= escolhido:
                break
        while True:
          posicao2 = choice(posicao)
          if 65 - posicao2 >= len(' '.join(palavra)):
              break
    #VERTICAL
    else:
        posicao2 = choice(posicao)
        while True:
            escolhido = choice(coluna)
            if 18 - len(palavra) >= escolhido:
                break
    if cordenadas == True:
        print(palavra)
        print('NA:',NA)
        print('Tipo:',tipo)
        print('linha:',escolhido)
        print('Posição:',posicao2)
    while not linhas == 18:
        while True:
            if c == 0:
                recepto += '|'
            #CONDIÇÃO PARA CAÇA PALAVRA NA HORIZONTAL
            if tipo == 'H':
                if escolhido == linhas and posicao2 == c:
                    recepto += palavra
                    c += len(palavra)
                else:
                    recepto += choice(lista)
                    c += 1
            # CONDIÇÃO PARA CAÇA PALAVRA NA VERTICAL
            elif tipo == 'V':
                if escolhido == linhas and posicao2 == c and cont < len(palavra):
                    recepto += palavra[cont]
                    escolhido += 1
                    cont += 1
                else:
                    recepto += choice(lista)
                    c += 1
            elif tipo == 'I':
                if escolhido == linhas and posicao2 == c and cont < len(palavra):
                    recepto += palavra[cont]
                    escolhido += 1
                    cont += 1
                    posicao2 += 2
                else:
                    recepto += choice(lista)
                    c += 1
            if len(recepto) < 65:
                recepto += ' '
                c += 1
            elif len(recepto) >= 65:
                recepto += '|\n'
                caca_palavras += recepto
                recepto = ''
                break
        linhas += 1
        c = 0
    print('+','-'* 63,'+')
    print(caca_palavras,end='')
    print('+','-'* 63,'+')
    usuario = ''
    chances = 5
    while True:
        usuario = input('Digite a Palavra:').upper()
        if chances == 0:
            print('SUAS CHANCES ACABARAM!')
            print('VOCÊ PERDEU')
            break
        if usuario == palavracorreta:
            print('VOCÊ ACERTOU!')
            print()
            break
        else:
            print('VOCÊ ERROU!')
            print(f'TENTE NOVAMENTE VOCÊ AINDA TEM {chances} TENTATIVAS')
        chances -= 1
