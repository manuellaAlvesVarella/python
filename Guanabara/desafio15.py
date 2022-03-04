carro = int(input('quantos dias o carro ficou alugado?'))
km = float(input('quantos km rodados?'))
total = (carro * 60)+(km * 0.15)
print ('valor total a pagar é de R${:.2f}'.format(total))