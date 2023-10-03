from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

import numpy as np

model = ResNet50(weights='imagenet')

def predictFunction(img, target_size, top_n=3):
    if img.size != target_size:
        img = img.resize(target_size)

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)

    return decode_predictions(preds, top=top_n)[0]

    # img_option dará as opções de pegar a imagem do diretório local ou de uma URL
    """ if img_option == 1:
        img_path = input("Digite o caminho da imagem: ")

        if not os.path.exists(img_path):
            print("Imagem não encontrada! Tente novamente.")
            return

        img = image.load_img(img_path, target_size=(224, 224))
        
        # Rodar a imagem com o opencv
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("Imagem", img)
        if cv2.waitKey(5) == 27:
            cv2.destroyAllWindows() """