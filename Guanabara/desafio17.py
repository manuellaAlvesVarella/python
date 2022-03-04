cp = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjente:'))
elevado = (cp**2 + ca**2) ** (1/2)
print ('a hipotenusa vai medir {:.2f}'.format(elevado))