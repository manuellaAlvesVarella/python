print ('{:=^40}'.format ('LOJAS ARICELIA'))
preço = float(input('Preço das compras: R$'))
print ('''FORMAS DE PAGAMENTO 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opição = int(input('Qual é a opição ?:'))
if opição == 1 : 
    total = preço - ( preço * 10 / 100 )
elif opição == 2 :
    total = preço - (preço * 5 / 100 )
elif opição == 3 :
    total = preço
    parcela = total / 2
    print ('Sua compra sera parcelada 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opição == 4 :
    total = preço + ( preço * 20 / 100 )
    totparc = int(input('quantas parcelas ? : '))
    parcela = total / totparc
    print ('Sua compra será parcelada em {}x de R${:.2f}COM JUROS'.format(totparc,parcela))
print ('Sua compra de {:.2f} vai custar R$ {:.2f} no final.'.format(preço,total))

