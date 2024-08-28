import cv2
import os

# Cargar la imagen
imagen = cv2.imread('../Imagenes/contorno.jpg')#Con los .. Se regresa una carpeta atras

# Verificar si la imagen fue cargada
if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta del archivo.")
    print("Directorio actual:", os.getcwd())
else:
    # Procede con el procesamiento de la imagen si se cargó correctamente
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _,umbral = cv2.threshold(gris,100,255,cv2.THRESH_BINARY)
    bordes = cv2.Canny(gris, 100, 200)
    contorno, jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imagen,contorno,-1,(251,60,50),3)#Con el menos 1 reconoce todos los contornos de la imagen
    #Mostrar
    cv2.imshow('imagen', imagen)
    cv2.imshow('Bordes Detectados', bordes)#Linea que pasa la imagen a una escala de grises
    cv2.imshow('Imagen Umbral', umbral)
    cv2.waitKey(0)
    cv2.destroyAllWindows()