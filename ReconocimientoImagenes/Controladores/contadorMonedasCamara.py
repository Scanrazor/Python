import cv2 

capturaVideo = cv2.VideoCapture(1)
if not capturaVideo.isOpened():
    print("No se encuentra una camara")
    exit()
while True:
    tipocamara, camara = capturaVideo.read()
    #grises = cv2.cvtColor(camara, cv2.COLOR_BAYER_BG2BGRA)

    cv2.imshow("En vivo",camara)
    if cv2.waitKey(1) == ord("q"):
        break

capturaVideo.release()
cv2.destroyAllWindows()