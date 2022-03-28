a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
c = int(input('terceiro valor:'))
menor = a 
if b < a and b < c :
    menor = b
if c < a and c < b :
    menor = c
maior = a
if b > a and b > c :
    maior = b
if c > a and c > b :
    maior = c
print ('O menor valor digitado foi {}'.format(menor))
print ('O maior valor digitado foi {}'.format(maior))