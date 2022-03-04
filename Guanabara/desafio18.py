import math 
ân = float(input('digite o ângulo que deseja:'))
seno = math.sin(math.radians(ân))
print ('O ângulo de {} tem o SENO de {:.2f}'.format(ân,seno))
cosseno = math.cos(math.radians(ân))
print ('O ângulo de {} tem o COSSENO de {:.2f}'.format(ân,cosseno))
tangente = math.tan (math.radians(ân))
print ('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ân,tangente))