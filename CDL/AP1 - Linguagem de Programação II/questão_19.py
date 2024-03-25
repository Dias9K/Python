import math
# Questão 19 – (1 ponto)
# GABRIEL MAGALHÃES DIAS
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6
# metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
# situações:
# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias.

preco_lata_18L = 80
litros_lata = 18
preco_galao_3_6L = 25
litros_galao = 3.6

print("Color Tintas Store".center(50, "="),
      "\nSeja muito bem vindo, a nossa loja está com promoções imperdíveis para você!!")
metros_quadrados = float(input("Digite em metros quadrados a área a ser pintada: "))

# calculando as quantidades das tintas
quantidade_litros = metros_quadrados/6
# o método math.ceil retornará um valor inteiro arredondado para o próximo número
quantidade_latas = math.ceil(quantidade_litros / litros_lata)
quantidade_galoes = math.ceil(quantidade_litros / litros_galao)
quantidade_mix = math.ceil()
# TODO calcular a quantidade e valor dos mixes
# calculando o valor dos casos (só latas, galões ou os dois juntos)
valor_apenas_latas = preco_lata_18L*quantidade_latas
valor_apenas_galoes = preco_galao_3_6L*quantidade_galoes
valor_mix =