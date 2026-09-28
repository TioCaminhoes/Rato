import time
import tkinter as tk

class labirintorato:
    
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.pilha = []
        self.visitados = []
        self.caminho = []
        
    def encontrar_caminho(self, inicio, fim):
        self.pilha.append(inicio)
        self.visitados.append(inicio)

        while self.pilha:
            posicao_atual = self.pilha.pop()
            self.caminho.append(posicao_atual)

            self.desenhar_labirinto_terminal(posicao_atual)
            time.sleep(0.4)

            if posicao_atual == fim:
                return self.caminho

            for vizinho in self.obter_vizinhos(posicao_atual):
                if vizinho not in self.visitados and self.labirinto[vizinho[0]][vizinho[1]] != 1:
                    self.pilha.append(vizinho)
                    self.visitados.append(vizinho)

        self.root.mainloop()
        return None

    def obter_vizinhos(self, posicao):
        x, y = posicao
        vizinhos = []

        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for dx, dy in movimentos:
            novo_x, novo_y = x + dx, y + dy
            if 0 <= novo_x < len(self.labirinto) and 0 <= novo_y < len(self.labirinto):
                vizinhos.append((novo_x, novo_y))

        return vizinhos

    def desenhar_labirinto_terminal(self, posicao_do_rato):
        print("\n--- RATO NO LABIRINTO ---")
        for i in range(len(self.labirinto)):
            linha_visual = ""
            for j in range(len(self.labirinto[i])):
                if (i, j) == posicao_do_rato:
                    linha_visual += " M "
                elif self.labirinto[i][j] == 1:
                    linha_visual += " 1 "
                else:
                    linha_visual += " 0 "
            print(linha_visual)

    def imprimir_caminho(self):
        for posicao in self.caminho:
            print(posicao)


labirinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

inicio = (0, 0)
fim = (4, 4)

labirinto_solver = labirintorato(labirinto)
caminho = labirinto_solver.encontrar_caminho(inicio, fim)

if caminho:
        print("\nCaminho completo percorrido (Histórico):")
        labirinto_solver.imprimir_caminho()
else:
        print("Nenhum caminho encontrado.")
