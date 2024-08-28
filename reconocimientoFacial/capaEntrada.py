import cv2 as cv
import numpy as np
import os
import imutils

modelo ='FotosElon'
ruta1 = 'C:/Users/roman/Desktop/python-webSite/reconocimientoFacial'
rutaCompleta = ruta1+'/'+ modelo

if not os.path.exists(rutaCompleta):
    os.makedirs(rutaCompleta)

ruidos = cv.CascadeClassifier('C:\\Users\\roman\\Desktop\\python-webSite\\entrenamiento opencv ruidos\\opencv-4.x\\data\\haarcascades\\haarcascade_frontalface_default.xml')
#camara = cv.VideoCapture(0)
camara = cv.VideoCapture("C:/Users/roman/Desktop/python-webSite/reconocimientoFacial/Data/ElonMusk.mp4")

id=0
while True :
    respuesta,captura=camara.read()
    if respuesta==False:break
    captura= imutils.resize(captura,width=640)


    grises = cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    cara= ruidos.detectMultiScale(grises, 1.3, 5)
    idCaptura= captura.copy()
    for(x,y,e1,e2) in cara:
        cv.rectangle(captura,(x,y), (x+e1,y+e2), (255,0,0),2)
        rostroCapturado = idCaptura[y:y+e2, x:x+e1]
        rostroCapturado = cv.resize(rostroCapturado,(160,160), interpolation=cv.INTER_CUBIC )
        cv.imwrite(rutaCompleta+'/imagen_{}.jpg'.format(id), rostroCapturado)
        id = id+1


    cv.imshow("Video",captura)

    if id==351:
        break
    if cv.waitKey(1) == ord("s"):
        break;

camara.release
cv.destroyAllWindows