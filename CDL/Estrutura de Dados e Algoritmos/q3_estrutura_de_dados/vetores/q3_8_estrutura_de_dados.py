# TODO fazer essa chibata rodar bem
# Implemente um algoritmo para encontrar o segundo maior valor em um vetor.
vetor = []

for i in range(5):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

maior = float('-inf')
segundo_maior = float('-inf')
for valor in vetor:
    if valor > maior:
        segundo_maior = maior
        maior = valor
    elif valor > segundo_maior and valor != maior:
        segundo_maior = valor

print(f"Números inseridos no vetor {vetor}\nE o seu segundo maior elemento do vetor é = {segundo_maior}")
