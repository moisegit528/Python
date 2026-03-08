def contador_personalizado():
    try:    
        limite = int(input("Digite um valor máximo: "))
        limite = limite + 1
        for i in range(limite):
            print(i)
            if i == limite:
                print("Contador atingiu o limite")
                break
    except ValueError:
        print("Entrada inválida. Por favor insira um número inteiro.")