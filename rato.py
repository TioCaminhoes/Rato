import time
import tkinter as tk

class labirintorato:
    
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.pilha = []
        self.visitados = set()
        self.caminho = []
        
        self.root = tk.Tk()
        self.root.title("Rato no Labirinto")
        self.tamanho_celula = 60
        self.canvas = tk.Canvas(
            self.root, 
            width=len(labirinto) * self.tamanho_celula, 
            height=len(labirinto) * self.tamanho_celula
        )
        self.canvas.pack()

    def encontrar_caminho(self, inicio, fim):
        self.pilha.append(inicio)
        self.visitados.add(inicio)

        while self.pilha:
            posicao_atual = self.pilha.pop()
            self.caminho.append(posicao_atual)

            self.desenhar_labirinto_terminal(posicao_atual)
            self.desenhar_interface_grafica(posicao_atual)
            time.sleep(0.4)

            if posicao_atual == fim:
                self.root.mainloop()
                return self.caminho

            for vizinho in self.obter_vizinhos(posicao_atual):
                if vizinho not in self.visitados and self.labirinto[vizinho[0]][vizinho[1]] != 1:
                    self.pilha.append(vizinho)
                    self.visitados.add(vizinho)

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
    def desenhar_interface_grafica(self, posicao_do_rato):
        self.canvas.delete("all")
        for i in range(len(self.labirinto)):
            for j in range(len(self.labirinto[i])):
                x1 = j * self.tamanho_celula
                y1 = i * self.tamanho_celula
                x2 = x1 + self.tamanho_celula
                y2 = y1 + self.tamanho_celula
                
                if self.labirinto[i][j] == 1:
                    cor = "#2C3E50"
                else:
                    cor = "#ECF0F1"
                    
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="#BDC3C7")
        
        rx1 = posicao_do_rato[1] * self.tamanho_celula + 15
        ry1 = posicao_do_rato[0] * self.tamanho_celula + 15
        rx2 = rx1 + self.tamanho_celula - 30
        ry2 = ry1 + self.tamanho_celula - 30
        self.canvas.create_oval(rx1, ry1, rx2, ry2, fill="#323232", outline="#323232")
        self.root.update()

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
