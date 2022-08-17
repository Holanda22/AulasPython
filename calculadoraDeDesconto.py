valor = float(input("Qual valor do produto? R$"))
porc = float(input("Qual porcentagem de desconto?"))

print("O produto de R${:.2f} com {:.0f}% de desconto sairá por R${:.2f}".format(
    valor, porc, (valor - ((valor*porc)/100))))
