"""
Problema das N-Rainhas
=======================
Implementação usando Busca em Profundidade (DFS) com backtracking.

O tabuleiro é representado como uma lista `posicoes`, onde `posicoes[i]`
indica a coluna em que a rainha da linha `i` está posicionada.
Como cada linha tem exatamente uma rainha, já evitamos conflitos de linha
automaticamente. Resta verificar conflitos de coluna e de diagonais.

A busca em profundidade explora a árvore de estados colocando uma rainha
por vez, linha após linha. Sempre que uma posição é inválida (conflito),
o algoritmo "poda" aquele ramo e retrocede (backtrack) para tentar outra
coluna — não avançando para as linhas seguintes. É esse corte antecipado
que torna o DFS eficiente para este problema, em vez de gerar todas as
permutações possíveis e testá-las no final.
"""

import time


def posicao_segura(posicoes, linha, coluna):
    """Verifica se é seguro colocar uma rainha em (linha, coluna),
    dado o que já foi colocado nas linhas anteriores (0..linha-1)."""
    for linha_anterior in range(linha):
        coluna_anterior = posicoes[linha_anterior]

        # mesma coluna
        if coluna_anterior == coluna:
            return False

        # mesma diagonal (principal ou secundária)
        if abs(coluna_anterior - coluna) == abs(linha_anterior - linha):
            return False

    return True


def dfs_n_rainhas(n, linha=0, posicoes=None, solucoes=None):
    """Busca em profundidade (DFS) com backtracking para o problema das N-Rainhas.

    Parâmetros:
        n         -- dimensão do tabuleiro (n x n) e número de rainhas
        linha     -- linha atual sendo preenchida (usado na recursão)
        posicoes  -- lista parcial de posições das rainhas (usado na recursão)
        solucoes  -- lista acumuladora de todas as soluções encontradas

    Retorna:
        lista de soluções, cada uma sendo uma lista `posicoes` completa
        (posicoes[i] = coluna da rainha na linha i)
    """
    if posicoes is None:
        posicoes = []
    if solucoes is None:
        solucoes = []

    # Caso base: todas as linhas foram preenchidas com sucesso -> solução válida
    if linha == n:
        solucoes.append(posicoes.copy())
        return solucoes

    # Tenta colocar a rainha da linha atual em cada coluna possível
    for coluna in range(n):
        if posicao_segura(posicoes, linha, coluna):
            posicoes.append(coluna)          # escolhe
            dfs_n_rainhas(n, linha + 1, posicoes, solucoes)  # aprofunda (DFS)
            posicoes.pop()                   # backtrack (desfaz a escolha)

    return solucoes


def imprimir_tabuleiro(posicoes, n):
    """Imprime uma representação visual do tabuleiro para uma solução."""
    for linha in range(n):
        linha_str = ""
        for coluna in range(n):
            linha_str += " D " if posicoes[linha] == coluna else " . "
        print(linha_str)
    print()


def main():
    tamanhos = [4, 5, 6, 7, 8]

    print("Problema das N-Rainhas — Busca em Profundidade (DFS/backtracking)")
    print("=" * 65)

    for n in tamanhos:
        inicio = time.time()
        solucoes = dfs_n_rainhas(n)
        duracao = time.time() - inicio

        print(f"\nTabuleiro {n}x{n}")
        print(f"  Total de soluções encontradas: {len(solucoes)}")
        print(f"  Tempo de execução: {duracao:.4f} s")

        if solucoes:
            print("  Exemplo de solução (posições por linha):", solucoes[0])
            print("  Representação visual:\n")
            imprimir_tabuleiro(solucoes[0], n)


if __name__ == "__main__":
    main()