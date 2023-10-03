from matplotlib import pyplot as plt

from src.structures.translatePredsFunction import translatePredsFunction

def plotFunction(image, preds):
    plt.imshow(image) # Mostrar imagem
    plt.axis('off') # Desativar eixos

    # Traduzir as predições para português
    translate = translatePredsFunction([pr[1] for pr in preds]) # [pr[1] for pr in preds] retorna uma lista com as predições em inglês

    # Gráfico de Barras
    plt.figure() # Criar figura
    order = list(reversed(range(len(preds)))) # Inverter a ordem da lista
    bar_preds = [pr[2] for pr in preds] # Lista com as probabilidades das predições
    labels = (tr for tr in translate) # Gerador de expressões para iterar sobre a lista translate
    plt.barh(order, bar_preds, alpha=0.5) # Criar gráfico de barras
    plt.yticks(order, labels) # Definir os rótulos do eixo y
    plt.xlabel('Predição/Probabilidade') # Definir rótulo do eixo x
    plt.xlim(0, 1.01) # Definir limites do eixo x
    plt.tight_layout() # Ajustar layout
    plt.show() # Mostrar gráfico