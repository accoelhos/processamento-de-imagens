# codigo da aula 24/02

# importacoes
import cv2 #visao computacional
import numpy # trabalhar com matrizes

# leitura da imagem com a funcao imread()
imagem = cv2.imread('gato-preto-deitado.jpg')
# a img eh armazenada na variavel imagem
# a imagem eh uma magriz de 3 dimensoes -> 3 canais RGB (red, green, blue), mas a ordem no python é bgr
# cada celula da matriz eh um pixel com valor de 0 a 255
# cada celula contem um inteiro de 8 bits sem sinal (uint8)
# cada pixel eh formado por uma tupla de 3 inteiros de 8 bits

# largura da imagem 
print('largura em pixels: ', imagem.shape[1])

# altura da imagem
print('altura em pixels: ', imagem.shape[0])

# qtd de canais da imagem (colorida possui 3 canais)
print('qtd de canais: ', imagem.shape[2])

# mostra img na tela com imshow
cv2.imshow('Nome da janela', imagem)
cv2.waitKey(0) # espera o usuario apertar uma tecla para fechar a janela

# salvar a img no disco com a funcao imwrite()
cv2.imwrite('imagem_copia.jpg', imagem) # salva a img com o nome 'imagem_copia.jpg'