# Documentação Img2Matrix

## Visão Geral

**Img2Matrix** é uma aplicação Python que converte imagens (PNG, JPG, BMP, PBM) em matrizes de pixels RGB e aplica transformações geométricas através de uma interface gráfica. Os usuários podem carregar uma imagem e aplicar várias transformações como rotação e espelhamento.

![Captura de Tela do Img2Matrix]("./Screenshot.png")

## Informações do Projeto

- **Título**: Operador de Imagens - Img2Matrix
- **Autor**: Victor Samir Ribeiro dos Anjos
- **Instituição**: Universidade Estadual do Sudoeste da Bahia (UESB)
- **Curso**: Ciência da Computação (GACV)
- **Versão**: 1.0
- **Data**: 5 de Janeiro de 2025
- **Licença**: MIT
- **Contato**: 202420500@uesb.edu.br

## Funcionalidades

- Carregamento de imagens em vários formatos (PNG, JPG, BMP, PBM)
- Conversão de imagens para representação matricial RGB
- Aplicação de transformações geométricas:
  - Rotação de 90° anti-horário
  - Rotação de 90° horário
  - Rotação de 180°
  - Espelhamento horizontal
  - Espelhamento vertical
- Exibição visual da imagem transformada
- Redimensionamento automático para ajustar ao canvas mantendo a proporção

## Requisitos

- Python 3.x
- Biblioteca Pillow (PIL)

## Instalação

1. Certifique-se de que o Python 3.x está instalado no seu sistema
2. Instale as dependências necessárias:

```bash
pip install Pillow
```

3. Baixe o arquivo `Img2Matrix.py`

## Uso

### Iniciando a Aplicação

Execute o script a partir do seu terminal ou prompt de comando:

```bash
python Img2Matrix.py
```

### Usando a Interface

1. Clique em "Carregar Imagem" para selecionar um arquivo de imagem
2. Uma vez que a imagem é carregada, os botões de transformação serão habilitados
3. Clique em qualquer um dos botões de transformação para aplicar a operação correspondente:
   - "Rotacionar 90°" - Rotação de 90° anti-horário
   - "Rotacionar -90°" - Rotação de 90° horário
   - "Rotacionar 180°" - Rotação de 180°
   - "Espelhar Horizontalmente" - Espelhamento horizontal
   - "Espelhar Verticalmente" - Espelhamento vertical
4. A imagem transformada será exibida no canvas

## Implementação Técnica

### Funções Principais

#### Conversão de Imagem

```python
def carregar_imagem(caminho):
    """
    Carrega uma imagem do caminho especificado e a converte para uma matriz RGB.
    
    Argumentos:
        caminho (str): Caminho para o arquivo de imagem
        
    Retorna:
        list: Lista 2D (matriz) onde cada elemento é uma tupla RGB (r,g,b)
    """
```

```python
def matriz_para_imagem(matriz):
    """
    Converte uma matriz RGB de volta para um objeto de Imagem PIL.
    
    Argumentos:
        matriz (list): Lista 2D de tuplas RGB
        
    Retorna:
        PIL.Image: A imagem resultante
    """
```

#### Operações de Matriz

```python
def transpor(matriz):
    """
    Transpõe uma matriz (troca linhas e colunas).
    
    Argumentos:
        matriz (list): Matriz de entrada 2D
        
    Retorna:
        list: Matriz transposta
    """
```

```python
def inverter_linhas(matriz):
    """
    Inverte a ordem dos elementos em cada linha.
    
    Argumentos:
        matriz (list): Matriz de entrada 2D
        
    Retorna:
        list: Matriz com linhas invertidas
    """
```

```python
def inverter_ordem_linhas(matriz):
    """
    Inverte a ordem das linhas na matriz.
    
    Argumentos:
        matriz (list): Matriz de entrada 2D
        
    Retorna:
        list: Matriz com ordem das linhas invertida
    """
```

#### Transformações

```python
def rotacionar_90(matriz):
    """
    Rotaciona a matriz 90 graus no sentido anti-horário.
    
    Argumentos:
        matriz (list): Matriz de entrada 2D
        
    Retorna:
        list: Matriz rotacionada
    """
```

```python
def rotacionar_180(matriz):
    """
    Rotaciona a matriz 180 graus.
    
    Argumentos:
        matriz (list): Matriz de entrada 2D
        
    Retorna:
        list: Matriz rotacionada
    """
```

```python
def rotacionar_90neg(matriz):
    """
    Rotaciona a matriz 90 graus no sentido horário.
    
    Argumentos:
        matriz (list): Matriz de entrada 2D
        
    Retorna:
        list: Matriz rotacionada
    """
```

### Implementação da Interface Gráfica

A aplicação utiliza Tkinter para a interface gráfica do usuário. Os componentes principais incluem:

- Botões para carregar imagens e aplicar transformações
- Canvas para exibir a imagem
- Métodos para lidar com interações do usuário e atualizar a exibição

## Fundamentos Matemáticos

### Transformações de Matriz

As transformações de imagem são implementadas como operações matemáticas em matrizes:

1. **Rotação**:
   - 90° anti-horário: Transposição + Inversão da ordem das linhas
   - 90° horário: Inversão da ordem das linhas + Transposição
   - 180°: Inversão da ordem das linhas + Inversão dos elementos em cada linha

2. **Espelhamento**:
   - Horizontal: Inversão dos elementos em cada linha
   - Vertical: Inversão da ordem das linhas

## Exemplos

### Exemplo 1: Carregando e Rotacionando uma Imagem

1. Inicie a aplicação
2. Clique em "Carregar Imagem" e selecione um arquivo de imagem
3. Clique em "Rotacionar 90°" para rotacionar a imagem 90 graus no sentido anti-horário
4. A imagem rotacionada será exibida no canvas

### Exemplo 2: Múltiplas Transformações

1. Carregue uma imagem
2. Clique em "Espelhar Horizontalmente" para espelhar a imagem horizontalmente
3. Clique em "Rotacionar 180°" para rotacionar a imagem espelhada em 180 graus
4. A imagem resultante terá passado por ambas as transformações

## Melhorias Potenciais

- Adicionar funcionalidade de exportação para salvar imagens transformadas
- Implementar transformações adicionais (escala, cisalhamento, etc.)
- Adicionar capacidades de desfazer/refazer
- Suporte para processamento em lote de múltiplas imagens
- Aprimorar a interface com miniaturas de pré-visualização para transformações
- Adicionar funções de manipulação de cores (escala de cinza, inversão de cores, etc.)

## Solução de Problemas

### Problemas Comuns

1. **Imagem Não Carrega**
   - Certifique-se de que o formato do arquivo é suportado (PNG, JPG, BMP, PBM)
   - Verifique se o caminho do arquivo contém caracteres especiais

2. **Problemas de Memória com Imagens Grandes**
   - A aplicação pode ter dificuldades com imagens muito grandes
   - Considere redimensionar imagens grandes antes de carregá-las

### Suporte

Para problemas, dúvidas ou sugestões, entre em contato:
- E-mail: 202420500@uesb.edu.br

## Referências

- [Documentação PIL/Pillow](https://pillow.readthedocs.io/)
- [Documentação TkInter GUI](https://docs.python.org/3/library/tkinter.html)
- [Operações de Matriz em Python](https://docs.python.org/3/tutorial/datastructures.html)

## Licença

Licença MIT

Copyright (c) 2025 Victor Samir Ribeiro dos Anjos

É concedida permissão, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e arquivos de documentação associados (o "Software"), para lidar com o Software sem restrições, incluindo, sem limitação, os direitos de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e permitir que as pessoas a quem o Software é fornecido o façam, sujeitas às seguintes condições:

O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM NENHUMA CIRCUNSTÂNCIA, OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, DELITO OU DE OUTRA FORMA, DECORRENTE DE, FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO SOFTWARE.