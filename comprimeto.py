M = float(input("Digite uma distância em metros:"))

print("A medida de {} metros corresponde à: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm".format(
    M, (M/1000), (M/100), (M/10), (M*10), (M*100), (M*1000)))
