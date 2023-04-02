import cv2

# Charger l'image à partir du fichier
image = cv2.imread('image.jpg')

# Convertir l'image en niveaux de gris pour faciliter la détection des visages
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Charger le classificateur de cascade de Haar pour la détection des visages
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Détecter les visages dans l'image en utilisant le classificateur de cascade de Haar
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Itérer sur les visages détectés et les découper en tant qu'images individuelles
for (x, y, w, h) in faces:
    # Découper le visage dans l'image d'origine
    face = image[y:y+h, x:x+w]
    # Enregistrer le visage découpé sous forme d'image individuelle
    cv2.imwrite('face_{}.jpg'.format(x), face)
