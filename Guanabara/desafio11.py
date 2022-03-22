largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
área = largura * altura 
resultado  = área / 2
print ('Sua parede tem a dimensão de {}X{} e sua área é de {}m2'.format(largura,altura,área))
print ('Para pintar essa parede ,você prescisa de {:.2f}L de tinta'.format(resultado))
