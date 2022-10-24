from time import sleep
import caca
jogador = ''
n = 'CAÇA PALAVRA'
print(f"+-+" * 7)
print(f'{n:^21}')
print(f"+-+" * 7)
print()
while True:
    print(f'''[1] Iniciar\n[2] Instruções\n[3] Sair''')
    usuario = input(f'ESCOLHA DO JOGADOR:')
    print('loading...')
    sleep(2)
    if usuario == '1':
        jogador = input('PRESS ENTER TO START')
        caca.caca(cordenadas=True)
    elif usuario == '2':
        print('-' * 60)
        print('''1 - Seu Objetivo é achar a palavra escondida entre as letras.
2 - A palavra pode estar na Horizontal,Vertical ou Inclinada e em todas essas
Formas ela pode está do avesso ou não.
3 - Ao Encontra a palavra  Informe a ao computador ele avaliará se está correto ou não
Você terá 5 chances para acerta caso todas elas sejam usadas a partida encerra e você perde.''',end='')
        input('')
        print('-' * 60)
    elif usuario == '3':
        print('Programa encerrado com sucesso.')
        break
    else:
        print('\033[31mOPÇÃO INVALIDA\033[m')
        continue