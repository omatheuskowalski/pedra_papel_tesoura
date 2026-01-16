import random


jogo = {
    'Pedra':'Tesoura',
    'Papel':'Pedra',
    'Tesoura':'Papel'
}

while True:
    escolha_computador  = random.choice(['Pedra', 'Papel', 'Tesoura'])
    escolha_usuario = input('Esolha ''Pedra'', ''Papel'' ou ''Tesoura'': ').capitalize()

    if escolha_usuario not in jogo:
        print('Opção inválida!\n')
        continue

    if escolha_usuario ==  escolha_computador:
        print('Houve um empate!')
    
    elif jogo[escolha_usuario] == escolha_computador:
        print(f'O usuário escolheu {escolha_usuario} e o computador escolheu {escolha_computador}.')
        print('O usuário venceu!')
    
    else:
        print(f'O usuário escolheu {escolha_usuario} e o computador escolheu {escolha_computador}.')
        print('O computador venceu!')

    continuar = input('Deseja jogar novamente? (Sim/Não): ').capitalize()
    
    if continuar != 'Sim':
        print('Encerrando programa.....')
        break
