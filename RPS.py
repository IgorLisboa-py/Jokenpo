while True:
    JN = 's'
    from random import randint
    from time import sleep
    itens = ('Pedra' ,'Papel' ,'Tesoura')
    computador = randint(0,2)
    print('''\nSuas opções
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura''')
    jogador = int(input('Qual é a sua jogada? '))
    print('JO')
    sleep(0.6)
    print('KEN')
    sleep(0.6)
    print('PO!')
    sleep(0.6)
    print('—'*42)
    print('\t\tO computador jogou: {}'.format(itens[computador]))
    print('\t\tO jogador jogou: {}'.format(itens[jogador]))
    print('—' *42)
    if computador == 0:
       if jogador == 0:
           print('\t\tEMPATE!')
       elif jogador == 1:
           print('\t\tJogador venceu!')
       elif jogador ==2:
           print('\t\tJogador perdeu!')
    elif computador == 1:
        if jogador == 0:
           print('\t\tJogador perdeu!')
        if jogador == 1:
           print('\t\tEMPATE!')
        if jogador == 2:
           print('\t\tJogador venceu!')
    elif computador == 2:
       if jogador == 0:
           print('\t\tJogador venceu!')
       if jogador == 1:
           print('\t\tJogador perdeu!')
       if jogador == 2:
           print('\t\tEMPATE!')
    JN = input('\n\t\tJogar Novamente? s/n ')
    if(JN =='n'):
        break
print('\n\t\tJogo finalizado!')
print('\n\t\tObrigado por jogar! =D')