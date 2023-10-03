from deep_translator import GoogleTranslator

def translatePredsFunction(text):
    # Criar um "for" para lidar com uma array de predições
    for i in range(len(text)):
        return GoogleTranslator(source='auto', target='pt').translate(text[i])