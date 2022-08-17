import math

print('Calculo de hipotenusa!')
c_a = float(input('Valor em centimetros do cateto adjacente:'))
c_o = float(input('Valor em centimetros do cateto oposto:'))
print('A hipotenusa deste triângulo retângulo é {:.2f} cm'.format(
    (math.hypot(c_a, c_o))))
    # sqrt((math.pow(c_a, 2))+(math.pow(c_o, 2)))
