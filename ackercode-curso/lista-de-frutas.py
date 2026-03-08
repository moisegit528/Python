frutas = ["Banana", "Maça", "Uva", "Pera", "Manga"]

for fruta in frutas:
    print(fruta)

# outra fomra utilizando input

frutas = []

while True:
    fruta = input("Digite o nome da fruta: ")
    if fruta == "sair":
        break
    frutas.append(fruta)

print(frutas)