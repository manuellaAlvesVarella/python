from datetime import date
data = date.today().year
ano = int(input('Ano de Nascimento:'))
dia = data - ano 
print ('O atleta  tem {} anos'.format(dia))
if dia < 9 :
    print('Classificação : MIRIM')
elif dia < 14 :
    print('Classificação : INFANTIL')
elif dia < 19 :
    print('Classificação : JUNIOR')
elif dia < 25 :
    print('Classificação : SÊNIOR')
else:
    print ('classificação : MASTER')