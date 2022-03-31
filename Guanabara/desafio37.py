num = int(input('Digite um número inteiro:'))
print ('''Escolha uma base para conversão:
[1] converte para BINÁRIO
[2] converta para OCTAL
[3] converta para HEXADECIMAL''')
opição = int(input('Sua opção: '))
if opição == 1:
    print ('{} convertido para BÍNARIO é igual a {}'.format(num,bin(num [2:])))
elif opição == 2:
    print ('{} convertido para OCTAL é igual a {}'.format(num,oct(num [2:])))
elif opição == 3:
    print ('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num [2:])))
else:
    print ('Opição inválida . Tente novamente')