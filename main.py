# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# chatbot = ChatBot('tester')
#
# conversa = [
#     'feliz aniversaio!',
#     'Ola tudo bem?',
#     'Feliz',
#     'bom dia tudo bem',
#     'Lol?',
#     'Só se for AGORA'
# ]
#
# trainer = ListTrainer(chatbot)
# trainer.train(conversa)
#
# chatbot.get_response("feliz aniversaio, Parabens, muitos anos de vida, MUITAS FELICIDSESDES MUITA ALEGRIA")


import cv2
import pytesseract

img = cv2.imread("ocr/img.png")
pytesseract.pytesseract.tesseract_cmd = 'ocr\\ocr.exe'

result= pytesseract.image_to_string(img)

print(result)
