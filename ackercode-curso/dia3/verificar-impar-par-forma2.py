entrada = input("Digite o número: ")
try:
    numero = int(entrada)
    if numero % 2 == 0:
        print("Número Par")
    else:
        print("Número Impar")
except ValueError:
    print("Você não digitou um número inteiro!")