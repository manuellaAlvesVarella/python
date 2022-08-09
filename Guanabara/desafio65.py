resp = 'S'
soma = quant = media = maior = menor = 0 
while resp in 'Ss':
    Num = int(input('Digite um número: '))
    soma += Num
    quant += 1
    if quant == 1 :
        maior = menor = Num
    else:
        if Num > maior:
            maior = Num
        if Num < menor:
            menor = Num 
    resp = str(input('Quer continuar(S/N)')).upper().strip()[0]
media = soma / quant
print ('Voce digitou {} numeros e a media foi {}'.format(quant,media))
print ('O maior numeros foi {} e o menor foi {}'.format(maior, menor))