# Imprimir o maior e menor número entre 5 inseridos pelo usuário.

maior = 0
menor = 0

for value in range(1, 6):
    var = int(input("Digite o " + str(value) + "° número :"))

    if range == 1:
        menor = var
        maior = var
    else:

        if var > maior:
            maior = var

        elif var < menor:
            menor = var

print("O maior número é: " + str(maior))
print("O menor número é: " + str(menor))
