# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.'
pares = 0

for i in range(1, 101):
    if i %2 == 0:
        pares = pares + i

print (pares)