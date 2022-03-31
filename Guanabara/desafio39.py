from datetime import date
data = date.today().year
ano = int(input('Ano de nascimento:'))
dia = data - ano 
print ('Quem nasceu no ano {} tem {} anos em {}'.format(ano,dia,data))
if dia == 18:
    print ('Você precisa se alistar IMEDIATAMENTE!')
elif dia < 18:
    saldo = 18 - dia
    print ('Ainda faltam {} anos para alistamento'.format(saldo))
elif dia > 18 :
    saldo = dia - 18
    print ('Você já deveria ter se alistado há {} anos'.format(saldo)) 

