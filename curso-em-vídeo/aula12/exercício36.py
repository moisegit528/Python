casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos de financiamento: "))
prestacao = casa / (anos * 12)
limite = salario * 30 / 100
if prestacao <= limite:
    print("Empréstimo APROVADO")
else:
    print("Empréstimo NEGADO")
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(casa, anos, prestacao))
