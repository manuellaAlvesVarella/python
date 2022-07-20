from pickle import TRUE
from random import randint
computador = randint (0, 10)
print ('sou seu computador... acabei de pensar em um número entre 0 e 10.')
print ('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0 
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = TRUE
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menor...Tente mais uma vez')
print('acertou com {} tentativas . Parabéns!'.format(palpites))