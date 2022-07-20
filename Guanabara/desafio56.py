somaidade = 0 
mediaidade = 0
maiordidaehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1,5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'Mm' and idade > maiordidaehomem:
        maiordidaehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20 :
        totmulher20 += 1
mediaidade = somaidade / 4
print ('A média idade do grupo é de {:.0f} anos'.format(mediaidade))
print ('o homem mais velho tem {} anos e se chama {}.'.format(maiordidaehomem,nomevelho))
print ('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))