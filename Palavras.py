def palavra():
    from random import choice
    ANIMAIS = choice(['CACHORRO','VACA','GATO','FOCA','TARTARUGA','RATO','COELHO','OVELHA'])
    OBJETO = choice(['FACA','CORDA','LAPÍS','CANETA','CELULAR','COPO','LATA','CHAVE','MOCHILA'])
    FRUTA = choice(['MAÇA','MANGA','KIWI','BANANA','LARANJA','LIMÃO','PÊSSEGO','ABACAXI','MORANGO'])

    ESCOLHIDO = choice([ANIMAIS,OBJETO,FRUTA])
    print(ESCOLHIDO)
    return str(ESCOLHIDO)