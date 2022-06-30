print ('=' * 31)
print ('    10 termos de um PA')
print ('=' * 31)
termo = int(input('primeiro termo:'))
razão = int(input('razão:'))
décimo = termo + (10 - 1) * razão
for c in range (termo , décimo + razão , razão) : 
    print('{}'.format(c), end=' - ')                
print ('!!ACABOU!!')
