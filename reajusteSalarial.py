print("Reajuste Salárial")
nome = input("Nome do funcionário:")
salárioAtual = float(input("Salário atual: R$"))
tipoReajuste = input("Tipo de reajuste:")
porc = float(input('Porcentagem de {}:'.format(tipoReajuste)))

if tipoReajuste == 'Aumento' or tipoReajuste == 'aumento':
    print('{} que recebe R${:.2f} irá ter {:.0f}% de aumento de salário e passará a receber R${:.2f}.'.format(
        nome, salárioAtual, porc, (salárioAtual+((salárioAtual*porc)/100))))
elif tipoReajuste == 'Redução' or tipoReajuste == 'redução':
    print('{} que recebe R${:.2f} irá ter {:.0f}% de redução de salário e passará a receber R${:.2f}.'.format(
        nome, salárioAtual, porc, (salárioAtual-((salárioAtual*porc)/100))))


