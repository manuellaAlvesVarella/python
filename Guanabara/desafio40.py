n1 = float(input('primeira nota:'))
n2 = float(input('segunda nota:'))
s = (n1 + n2) / 2  
print ('Tirando {} e {}, a média do aluno é {}'.format(n1,n2,s))
if s < 5.0:
    print ('O aluno está REPROVADO!')
elif s > 5.0 and 6.9:
    print ('O aluno está de RECUPERAÇÃO!')
elif s + 7.0 :
    print ('O aluno está APROVADO!')