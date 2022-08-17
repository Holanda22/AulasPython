real = float(input("Quanto você possui na sua carteira hoje? R$"))
dolar = real/5.17
euro = real/5.29

print("Com R${:.2f} é possível comprar U${:.2f} ou EUR{:.2f}".format(
    real, dolar, euro))
