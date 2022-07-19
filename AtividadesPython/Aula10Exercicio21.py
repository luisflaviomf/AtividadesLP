# Ler uma matriz 4x5 de inteiros, calcular e imprimir a soma de todos os seus
# elementos e soma dos elementos por coluna.

linha = 4
coluna = 5
total = 0
AUX = 0
somacolunas = [0]*5
# Criação da matriz
matriz = [[None for i in range(5)] for i in range(6)]

# Pegar valores da matriz
for j in range(coluna):
    for i in range(linha):
        matriz[i][j] = int(input(f"Digite um numero: L:{i} C:{j} = "))
        total = total + matriz[i][j]
        somacolunas[AUX] = somacolunas[AUX] + matriz[i][j]
    AUX+=1

# Mostrar soma de todos os valores de cada coluna
print(somacolunas)
# Mostrar soma de todos os valores da matriz
print(total)