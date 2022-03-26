distância = float(input('Qua é a distância da viagem ?:'))
print ('Você esta preste a começar sua viagem de {} Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else :
    preço = distância * 0.45
print ('E o preço da sua passagem sará de R${:.2f}'.format(preço))

