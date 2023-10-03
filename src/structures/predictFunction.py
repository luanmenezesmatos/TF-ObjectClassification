from keras.preprocessing import image # Importar módulo de pré-processamento de imagens do Keras
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions # Importar modelo ResNet50, pré-processamento e decodificação de predições

import numpy as np # Importar numpy

model = ResNet50(weights='imagenet') # Carregar modelo ResNet50 com os pesos do ImageNet

# Função para fazer a predição da imagem
def predictFunction(img, target_size, top_n=3):
    if img.size != target_size: # Verificar se o tamanho da imagem é diferente do tamanho que o modelo espera
        img = img.resize(target_size) # Redimensionar a imagem

    x = image.img_to_array(img) # Converter a imagem para um array
    x = np.expand_dims(x, axis=0) # Adicionar uma dimensão extra para o array
    x = preprocess_input(x) # Pré-processar o array

    preds = model.predict(x) # Fazer a predição

    return decode_predictions(preds, top=top_n)[0] # Decodificar as predições e retornar apenas as top_n predições