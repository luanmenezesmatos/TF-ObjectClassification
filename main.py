from src.structures.selectOption import selectOption # Função para fazer a pergunta e mostrar as opções
from src.structures.predictFunction import predictFunction # Função para fazer a predição da imagem
from src.structures.plotFunction import plotFunction # Função para plotar a imagem e o gráfico de barras
from src.structures.handleError import handleError # Classe para tratar erros
from src.structures.handleUtil import handleUtil # Classe de verificações necessárias para o funcionamento do programa

from PIL import Image # Biblioteca para trabalhar com imagens

import requests # Biblioteca para trabalhar com requisições HTTP, nesse caso, com as imagens da URL

select = selectOption("Qual será o tipo de imagem que você irá enviar?", ["Arquivo de Imagem", "URL de Imagem"]).choose()
match select:
    case 1:
        img_path = input("Digite o caminho da imagem: ")

        # Verificar se o caminho informado existe usando o os.path.exists()
        if not handleUtil(img_path).verifyLocalPath():
            handleError("O caminho informado não existe!", 404).sendErrorMessage()
            exit()

        img = Image.open(img_path)

        preds = predictFunction(img, target_size=(224, 224))
        plotFunction(img, preds)
    case 2:
        img_url = input("Digite a URL da imagem: ")

        # Verificar se a URL informada existe usando o requests.get()
        if not handleUtil(img_url).verifyUrl():
            handleError("A URL informada não existe!", 404).sendErrorMessage()
            exit()

        # Verificar se a URL informada é uma imagem usando o requests.get()
        if not handleUtil(img_url).verifyContentTypeHeader():
            exit()

        # Verificar se a URL informada não é um arquivo do diretório local
        if handleUtil(img_url).verifyLocalPath():
            handleError("Nós só permitimos imagens que estejam em um servidor!", 403).sendErrorMessage()
            exit()

        # Abrir a imagem usando o Image.open() e o requests.get() com o stream=True (para não carregar a imagem inteira na memória)
        img = Image.open(requests.get(img_url, stream=True).raw)

        preds = predictFunction(img, target_size=(224, 224))
        plotFunction(img, preds)
    case _: # Caso o usuário digite uma opção inválida
        handleError("Opção inválida! Tente novamente.", 400).sendErrorMessage()
        exit()