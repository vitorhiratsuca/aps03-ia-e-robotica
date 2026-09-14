"""
Problema das N-Rainhas
=======================
O estado do problema (`NRainhasState`) representa um tabuleiro parcial:
`posicoes[i]` é a coluna da rainha da linha `i`. Como cada linha recebe
no máximo uma rainha, conflitos de linha já são evitados por
construção. O método `successors()` só gera os sucessores em que a
nova rainha não ataca nenhuma das já colocadas (mesma coluna ou mesma
diagonal) — é esse filtro que poda os ramos inválidos da árvore de
busca. Quem percorre essa árvore (empilhar, aprofundar e retroceder ao
esvaziar um ramo) é o próprio `BuscaProfundidade` da aigyminsper.
"""

import time

from aigyminsper.search.graph import State
from aigyminsper.search.search_algorithms import BuscaProfundidade


class NRainhasState(State):
    """Estado do problema das N-Rainhas: tabuleiro parcial N x N.

    `posicoes` é uma tupla em que `posicoes[i]` é a coluna da rainha
    colocada na linha `i` (linhas de 0 até len(posicoes) - 1).
    """

    def __init__(self, n, posicoes=(), operator=""):
        super().__init__(operator)
        self.n = n
        self.posicoes = posicoes

    def _segura(self, coluna):
        """Verifica se colocar uma rainha na próxima linha, na coluna
        informada, não gera conflito."""
        linha = len(self.posicoes)
        for linha_anterior, coluna_anterior in enumerate(self.posicoes):
            mesma_coluna = coluna_anterior == coluna
            mesma_diagonal = abs(coluna_anterior - coluna) == abs(linha_anterior - linha)
            if mesma_coluna or mesma_diagonal:
                return False
        return True

    def successors(self):
        linha = len(self.posicoes)
        estados_sucessores = []
        for coluna in range(self.n):
            if self._segura(coluna):
                novas_posicoes = self.posicoes + (coluna,)
                operador = f"rainha da linha {linha} na coluna {coluna}"
                estados_sucessores.append(NRainhasState(self.n, novas_posicoes, operador))
        return estados_sucessores

    def is_goal(self):
        return len(self.posicoes) == self.n

    def description(self):
        return f"Problema das {self.n}-Rainhas"

    def cost(self):
        return 1

    def env(self):
        return str(self.posicoes)


def imprimir_tabuleiro(posicoes, n):
    for linha in range(n):
        linha_str = ""
        for coluna in range(n):
            linha_str += " D " if posicoes[linha] == coluna else " . "
        print(linha_str)
    print()


def main():
    tamanhos = [4, 5, 6, 7, 8]
    algoritmo = BuscaProfundidade()

    print("Problema das N-Rainhas — Busca em Profundidade")
    print("=" * 79)

    for n in tamanhos:
        estado_inicial = NRainhasState(n)
        inicio = time.time()
        solucao = algoritmo.search(estado_inicial, m=n, pruning="without")
        duracao = time.time() - inicio

        print(f"\nTabuleiro {n}x{n}")
        if solucao is None:
            print("  Nenhuma solução encontrada.")
            continue

        posicoes = solucao.state.posicoes
        print(f"  Solução (posições por linha): {list(posicoes)}")
        print(f"  Tempo de execução: {duracao:.4f} s")
        print("  Representação visual:\n")
        imprimir_tabuleiro(posicoes, n)


if __name__ == "__main__":
    main()
