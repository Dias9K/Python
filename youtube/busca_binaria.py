# o algoritmo de busca binária basicamente trabalha dividindo o vetor no meio e o comparando até achar o elemento que
# se está buscando

def busca_binaria(vet, ponto_inicial, ponto_final, elemento):  # o algoritmo recebe como parâmetros o vetor, o posição
    # inicial, a final e o elemento que se deseja procurar
    if ponto_inicial <= ponto_final:  # o vetor precisa ter ao menos um elemento
        meio = (ponto_inicial + ponto_final) // 2  # descobrindo o índice do meio do vetor
        # se o meio for maior do que o elemento escolhido fará a mesma coisa, porém com a parte da direita
        if elemento > vet[meio]:
            return busca_binaria(vet, meio + 1, ponto_final, elemento)
        # o vetor será reduzido para a parte da esquerda e dessa parte, fará a mesma verificação;
        elif elemento < vet[meio]:
            return busca_binaria(vet, ponto_inicial, meio - 1, elemento)
        # se o meio do vetor for o elemento escolhido, o código para se o meio for menor do que o elemento escolhido,
        else:
            return meio
    return -1


vetor = list(range(0, 10))
# print(busca_binaria(vetor, 0, 10, 9))
