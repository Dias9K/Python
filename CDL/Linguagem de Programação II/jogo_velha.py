velha = """
                   -- POSICOES --
       |   |         1 | 2 | 3
    -----------     -----------
       |   |         4 | 5 | 6
    -----------     -----------
       |   |         7 | 8 | 9
"""

print(velha)
ganho = [
    # linha
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    # coluna
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
    # diagonal
    [7, 5, 3],
    [9, 5, 1]
]
