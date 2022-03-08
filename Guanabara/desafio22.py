frase = str(input('digite o seu nome completo :')).strip()
print ('analizando o seu nome...')
print ('seu nome em letras maiúscula é {}'.format(frase.upper()))
print ('seu nome em letras minúsculas é {}'.format(frase.lower()))
print ('seu nome tem ao todo {} letras'.format(len(frase) - frase.count(' ')))
print ('seu primeiro nome tem {} letras'.format(frase.find(' ')))



