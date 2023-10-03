from src.structures.selectOption import selectOption # Função para fazer a pergunta e mostrar as opções
from src.structures.predictFunction import predictFunction # Função para fazer a predição da imagem
from src.structures.plotFunction import plotFunction # Função para plotar a imagem e o gráfico de barras

from PIL import Image # Biblioteca para trabalhar com imagens

import requests # Biblioteca para trabalhar com requisições HTTP, nesse caso, com as imagens da URL

select = selectOption("Qual será o tipo de imagem que você irá enviar?", ["Arquivo de Imagem", "URL de Imagem"]).choose()
match select:
    case 1:
        img_path = input("Digite o caminho da imagem: ")
        img = Image.open(img_path)

        preds = predictFunction(img, target_size=(224, 224))
        plotFunction(img, preds)
    case 2:
        img_url = input("Digite a URL da imagem: ")
        img = Image.open(requests.get(img_url, stream=True).raw)

        preds = predictFunction(img, target_size=(224, 224))
        plotFunction(img, preds)
    case _:
        print("Opção inválida! Tente novamente.")