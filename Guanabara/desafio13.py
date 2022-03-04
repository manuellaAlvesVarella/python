preço = float(input('qual é o salario desse funcionário?:'))
novo = preço + (preço *15/100)
print ('Um funcionário que ganhava {:.2f} reais,com 15 porcento de almento,passa a ganhar {:.2f}'.format(preço,novo))