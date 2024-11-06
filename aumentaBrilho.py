from PIL import Image

# Carregar a imagem
imagem = Image.open("arquivo_5bits.pgm")

# Converter a imagem para o modo RGB (caso não esteja)
imagem = imagem.convert("RGB")

# Aplicar o ganho de brilho
fator_ganho = 1.2  # 20% de aumento
imagem_brilho = imagem.point(lambda p: min(int(p * fator_ganho), 255))

# Salvar ou exibir a imagem
imagem_brilho.save("imagem_com_mais_brilho.jpg")
imagem_brilho.show()
