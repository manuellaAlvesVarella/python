valor = float(input('Valor da casa: R$'))
salário = float(input('salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento ?:'))
prestação = valor / (anos * 12)
mínimo = salário * 30 / 100
print ('Para pagar uma casa de R$ {:.2f} em {} anos'.format(valor , anos))
print ('A prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print ('Empréstimo pode ser CONCEDIDO!!!')
else:
    print ('Empréstimo NEGADO!')
