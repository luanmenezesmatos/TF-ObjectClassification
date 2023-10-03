from src.structures.handleError import handleError

import requests
import os

class handleUtil:
    def __init__(self, img_path):
        self.img_path = img_path

    def verifyUrl(self):
        try:
            if requests.get(self.img_path).status_code == 200:
                return True
        except:
            return False
        
    def verifyLocalPath(self):
        if os.path.exists(self.img_path):
            return True
        
        return False

    def verifyContentTypeHeader(self):
        verifyContentTypeHeader = requests.get(self.img_path).headers['Content-Type'].split('/')[0]

        translateContentTypeHeader = {'image': 'imagem', 'video': 'vídeo', 'audio': 'áudio'}

        if not verifyContentTypeHeader == 'image':
            contentTypeTranslation = translateContentTypeHeader.get(verifyContentTypeHeader, 'página')
            handleError(f"A URL informada não é uma imagem e sim um(a) {contentTypeTranslation}", 403).sendErrorMessage()
            return False
        
        return True