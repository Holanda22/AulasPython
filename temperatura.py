C = float(input("Digite uma temperatura em graus Celsius:"))

print("Temperatura nas escalas: \nFahrenheit: {:.1f} \nKelvin: {:.1f} \nRéaumur: {:.1f} \nRankine: {:.1f}".format(
    (C*1.8+32), (C+273.15), (C*0.8), (C+1.8+32+459.67)))
