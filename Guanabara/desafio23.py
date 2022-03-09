frase = int(input('digite um número:'))
u = frase // 1    %  10
d = frase // 10   %  10
c = frase // 100  %  10
m = frase // 1000 %  10
print ('analizando o número {}'.format(frase)) 
print ('unidade = {}'.format(u))
print ('dezena = {}'.format(d))
print ('centena = {}'.format(c))
print ('milhar = {}'.format (m))