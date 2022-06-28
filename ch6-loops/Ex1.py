# Programa para determinar os 5 primeiros multiplos de 3 a partir de um número escolhido, maior do que zero.

number = int(input("Digite um número:"))

if number > 0:
    if number % 3 == 0:
        end = 4
        print(number)
        number = number + 3
    else:
        end = 5

    for value in range(0, end):
        while number % 3 != 0:
            number += 1
        print(number)
        number += 3

else:
    end = None
    print("O programa aceita apenas números maiores que 0.")
