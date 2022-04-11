soma = 0
cont = 0
for c in range (1,501,2) :
    if c % 3 == 0 :
        cont = cont + 1 # geralmente um cont ou contador conta mais 1
        soma = soma + c # geralmente o aculador nesse caso o 'soma' ele vai fazer o papel de adição ou mutplicação
print ('A soma de todos os {} valores solicidados é {}'.format(cont,soma))