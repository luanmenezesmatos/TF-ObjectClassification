from deep_translator import GoogleTranslator

def translatePredsFunction(predictions, source_lang='auto', target_lang='pt'):
    translated_preds = []

    for prediction in predictions:
        translated_preds.append(GoogleTranslator(source=source_lang, target=target_lang).translate(prediction).replace("_", " ").title())
        # translate() retorna uma string, logo, é possível usar o método title() para deixar a primeira letra de cada palavra maiúscula
        # replace() substitui "_" por " " (espaço) para melhorar a legibilidade

    return translated_preds