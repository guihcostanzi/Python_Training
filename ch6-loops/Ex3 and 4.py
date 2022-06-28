# Contagem regressiva com while.

start = 10
while start != 0:
    print(start)
    start -= 1
print("End.")

print("------------------------------------")

# Executar até chegar em cem mil e dizer quantas adições foram feitas.

start = 0
count = 0
while start < 10**5:
    start += 1000
    count += 1
print(count)
