"""
Img2Matrix.py

@title: Operador de Imagens - Img2Matrix
@description: 
    Converte imagens (PNG, JPG, BMP, PBM) em matrizes de pixels RGB e aplica transformações 
    geométricas (rotações e espelhamentos) via interface gráfica.
@author: Victor Samir Ribeiro dos Anjos
@institution: Universidade Estadual do Sudoeste da Bahia (UESB)
@course: Ciência da Computação (GACV)
@date: 2025-01-05
@version: 1.0
@license: MIT (ou "Uso acadêmico livre")
@requirements: Python 3.x, Pillow (pip install Pillow)
@usage: 
    1. Execute: python Img2Matrix.py
    2. Na GUI: Carregue uma imagem e use os botões para transformações.
@references:
    - PIL/Pillow Documentation: https://pillow.readthedocs.io/
    - TkInter GUI: https://docs.python.org/3/library/tkinter.html
"""
__author__ = "Victor Samir Ribeiro dos Anjos"
__version__ = "1.0"
__date__ = "2025-01-05"
__copyright__ = "© 2025 Victor Samir Ribeiro dos Anjos (Uso acadêmico)"
__license__ = "MIT"
__email__ = "202420500@uesb.edu.br"

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Carrega a imagem e converte para matriz
def carregar_imagem(caminho):
    imagem = Image.open(caminho).convert('RGB')
    largura, altura = imagem.size
    pixels = imagem.load()

    matriz = []
    for y in range(altura):
        linha = []
        for x in range(largura):
            linha.append(pixels[x, y])
        matriz.append(linha)
    return matriz

# Salva e mostra a imagem
def matriz_para_imagem(matriz):
    altura = len(matriz)
    largura = len(matriz[0])
    nova_img = Image.new('RGB', (largura, altura))
    for y in range(altura):
        for x in range(largura):
            nova_img.putpixel((x, y), matriz[y][x])
    return nova_img

# Transpor matriz
def transpor(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    transposta = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)
    return transposta

# Inverter ordem dos elementos na linha
def inverter_linhas(matriz):
    invertida = []
    for linha in matriz:
        nova = []
        for i in range(len(linha)-1, -1, -1):
            nova.append(linha[i])
        invertida.append(nova)
    return invertida

# Inverter ordem das linhas
def inverter_ordem_linhas(matriz):
    invertida = []
    for i in range(len(matriz)-1, -1, -1):
        invertida.append(matriz[i])
    return invertida

# Operações
# Rotação de 90° anti-horário
def rotacionar_90(matriz):
    return inverter_ordem_linhas(transpor(matriz))

# Rotação de 180°
def rotacionar_180(matriz):
    return inverter_linhas(inverter_ordem_linhas(matriz))

# Rotação de 90° horário
def rotacionar_90neg(matriz):
    return transpor(inverter_ordem_linhas(matriz))

# interface gráfica
class App:

    def redimensionar_imagem(self, imagem, largura_max, altura_max):
        # Obtém as dimensões originais da imagem
        img_largura, img_altura = imagem.size

        # Calcula a relação de aspecto
        proporcao_largura = largura_max / img_largura
        proporcao_altura = altura_max / img_altura

        # Usa a menor proporção para redimensionar a imagem proporcionalmente
        proporcao = min(proporcao_largura, proporcao_altura)

        # Calcula as novas dimensões
        nova_largura = int(img_largura * proporcao)
        nova_altura = int(img_altura * proporcao)

        try:
            resample = Image.Resampling.LANCZOS
        except AttributeError:
            resample = Image.ANTIALIAS

        # Redimensiona a imagem
        return imagem.resize((nova_largura, nova_altura), resample)
    
    def habilitar_botoes(self):
        self.botao_90.config(state=tk.NORMAL)
        self.botao_180.config(state=tk.NORMAL)
        self.botao_90neg.config(state=tk.NORMAL)
        self.botao_espelhar_h.config(state=tk.NORMAL)
        self.botao_espelhar_v.config(state=tk.NORMAL)

    def exibir_matriz(self):
        imagem = matriz_para_imagem(self.matriz)
        
        # Obtém as dimensões do canvas
        canvas_largura = self.canvas.winfo_width()
        canvas_altura = self.canvas.winfo_height()

        # Redimensiona a imagem para caber no canvas, proporcionalmente
        imagem = self.redimensionar_imagem(imagem, canvas_largura, canvas_altura)

        # Converte a imagem para um formato que o tkinter pode usar
        self.imgtk = ImageTk.PhotoImage(imagem)

        # Limpa o canvas antes de desenhar a nova imagem
        self.canvas.delete("all")

        # Obtém as novas dimensões da imagem
        img_largura = imagem.width
        img_altura = imagem.height

        x = (canvas_largura - img_largura) // 2
        y = (canvas_altura - img_altura) // 2

        # Exibe a imagem centralizada no canvas
        self.canvas.create_image(x, y, anchor=tk.NW, image=self.imgtk)

        # Ajusta a região qua pode ser visualizada
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

    def abrir_imagem(self):
        caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *pbm")])
        if caminho:
            self.caminho = caminho
            self.matriz = carregar_imagem(caminho)
            self.label.config(text=f"Imagem carregada com sucesso!")
            self.exibir_matriz()
            self.habilitar_botoes()

    def aplicar_rotacao_90(self):
        self.matriz = rotacionar_90(self.matriz)
        self.exibir_matriz()

    def aplicar_rotacao_180(self):
        self.matriz = rotacionar_180(self.matriz)
        self.exibir_matriz()

    def aplicar_rotacao_90neg(self):
        self.matriz = rotacionar_90neg(self.matriz)
        self.exibir_matriz()

    def aplicar_espelhamento_h(self):
        self.matriz = inverter_linhas(self.matriz)
        self.exibir_matriz()

    def aplicar_espelhamento_v(self):
        self.matriz = inverter_ordem_linhas(self.matriz)
        self.exibir_matriz()

    def __init__(self, master):
        self.master = master
        master.title("Img2Matrix")

        self.label = tk.Label(master, text="Escolha uma imagem:")
        self.label.pack()

        self.botao_carregar = tk.Button(master, text="Carregar Imagem", command=self.abrir_imagem)
        self.botao_carregar.pack(pady=5)

        self.botao_90 = tk.Button(master, text="Rotacionar 90°", command=self.aplicar_rotacao_90, state=tk.DISABLED)
        self.botao_90.pack(pady=5)

        self.botao_90neg = tk.Button(master, text="Rotacionar -90°", command=self.aplicar_rotacao_90neg, state=tk.DISABLED)
        self.botao_90neg.pack(pady=5)
        
        self.botao_180 = tk.Button(master, text="Rotacionar 180°", command=self.aplicar_rotacao_180, state=tk.DISABLED)
        self.botao_180.pack(pady=5)

        self.botao_espelhar_h = tk.Button(master, text="Espelhar Horizontalmente", command=self.aplicar_espelhamento_h, state=tk.DISABLED)
        self.botao_espelhar_h.pack(pady=5)

        self.botao_espelhar_v = tk.Button(master, text="Espelhar Verticalmente", command=self.aplicar_espelhamento_v, state=tk.DISABLED)
        self.botao_espelhar_v.pack(pady=5)

        # Canvas para exibir a imagem
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.caminho = None
        self.matriz = None


# Executar
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

