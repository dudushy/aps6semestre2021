import cv2
import face_recognition
import os

caminho = r'C:\Users\User\Documents\DriveSync\0FACULDADE\0 UNIP\APS - Atividades Práticas Supervisionadas\APS 6º Semestre\faces'
imagens = []
classeNomes = []
minhaLista = os.listdir(caminho)
#print(minhaLista)

for item in minhaLista:
    imgAtual = cv2.imread(f'{caminho}/{item}')
    imagens.append(imgAtual)
    classeNomes.append(os.path.splitext(item)[0])
print("\n")
print(classeNomes)

def encontrarEncodamento(images):
    listaEncodamento = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodamento = face_recognition.face_encodings(img)[0]
        listaEncodamento.append(encodamento)
    return listaEncodamento

listaEncodamentoConhecida = encontrarEncodamento(imagens)
print('encodamento completo')
print(len(listaEncodamentoConhecida))
