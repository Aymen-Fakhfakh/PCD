import cv2
import time

# Configuration de la caméra
cam = cv2.VideoCapture(0) # Ouverture de la caméra

# Boucle principale
while True:
    # Capture d'une image
    ret, frame = cam.read()

    # Vérification de la capture
    if not ret:
        print("La capture a échoué.")
        break

    # Traitement de l'image (facultatif)

    # Enregistrement de l'image
    filename = f"capture_{time.strftime('%Y%m%d_%H%M%S')}.jpg"
    cv2.imwrite(filename, frame)

    # Attente de 5 minutes
    time.sleep(300)

    # Lecture de l'image enregistrée et renvoi du résultat
    result = cv2.imread(filename)
    
