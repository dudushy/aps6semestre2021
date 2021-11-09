import cv2
import face_recognition
import numpy as np
import os

caminho = 'rostos'
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

capt = cv2.VideoCapture(0)

while True:
    sucess, img = capt.read()
    imgS = cv2.resize(img, (0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)


    rostoAtual = face_recognition.face_locations(imgS)
    encodamentoAtual = face_recognition.face_encodings(imgS, rostoAtual)

    for rostoEncodado, rostoLoc in zip(encodamentoAtual,rostoAtual):
        encaixe = face_recognition.compare_faces(listaEncodamentoConhecida, rostoEncodado)
        distanciaRosto = face_recognition.face_distance(listaEncodamentoConhecida,rostoEncodado)
        print(distanciaRosto)
        encaixeAmbas = np.argmin(distanciaRosto)

        if encaixe[encaixeAmbas]:
            nome = classeNomes[encaixeAmbas].upper()
            print(nome)
            y1,x2,y2,x1 = rostoLoc
            y1,x2,y2,x1 = y1+4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,nome,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


    cv2.imshow('Webcam', img)
    cv2.waitKey(1)