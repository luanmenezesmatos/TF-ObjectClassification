from matplotlib import pyplot as plt

from src.structures.translatePredsFunction import translatePredsFunction

def plotFunction(image, preds):
    plt.imshow(image)
    plt.axis('off')

    # Traduzir as predições para português
    # preds = translatePredsFunction([pr[1] for pr in preds])
    # translatePredsFunction([pr[1] for pr in preds])
    translatedWordsArr = []

    for i in range(len(preds)):
        translatedWordsArr.append(translatePredsFunction([pr[1] for pr in preds]))
        print(translatedWordsArr[i])

    # Gráfico de Barras
    plt.figure()
    order = list(reversed(range(len(preds))))
    bar_preds = [pr[2] for pr in preds]
    labels = (pr[1] for pr in preds)
    plt.barh(order, bar_preds, alpha=0.5)
    plt.yticks(order, labels)
    plt.xlabel('Predição/Probabilidade')
    plt.xlim(0, 1.01)
    plt.tight_layout()
    plt.show()