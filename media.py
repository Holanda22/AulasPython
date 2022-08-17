print("CALCULADORA DE MÉDIA ESCOLAR")
nota_mat = float(input("Matemática:"))
nota_port = float(input("Português:"))
nota_cie = float(input("Ciências:"))
nota_geo = float(input("Geografia:"))
nota_hist = float(input("História:"))

nome = input("Nome do(a) aluno(a):")

print("A média de {} é: {:.1f}.".format(
    nome, ((nota_mat+nota_port+nota_cie+nota_geo+nota_hist)/5)))
