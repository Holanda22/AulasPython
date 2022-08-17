num = int(input("Digite o número que deseja saber a tabuada:"))

print("-" * 14, "\nTabuada do {}:".format(num))
for x in range(1, 11):
    print("{} x {} = {}".format(x, num, (x*num)))
print("-" * 14)