from keras.models import load_model
import cv2
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("/Users/joaovyctor/Documents/TG-Fatec/TG-DRONE/ReconView/keras_model.h5", compile=False)

# Load the labels
class_names = open("/Users/joaovyctor/Documents/TG-Fatec/TG-DRONE/ReconView/labels.txt", "r").readlines()

# Defina a largura e a altura desejadas para a janela
window_width = 800
window_height = 600

# CAMERA pode ser 0 ou 1 com base na câmera padrão do seu computador
camera = cv2.VideoCapture(0)
camera.set(3, 1920)  # Largura da resolução
camera.set(4, 1080)  # Altura da resolução

while True:
    # Captura a imagem da webcam.
    ret, image = camera.read()

    # Redimensiona a imagem bruta para as dimensões desejadas.
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Mostra a imagem em uma janela redimensionada.
    cv2.imshow("Webcam Image", cv2.resize(image, (window_width, window_height)))

    # Restante do código...

    # Make the image a numpy array and reshape it to the model's input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Escute o teclado para pressionamentos de tecla.
    keyboard_input = cv2.waitKey(1)

    # 27 é o código ASCII para a tecla Esc no teclado.
    if keyboard_input == 27:
        break

# Libera a câmera e fecha todas as janelas abertas.
camera.release()
cv2.destroyAllWindows()
