from keras.models import load_model
import cv2
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("/Users/joaovyctor/Documents/TG-Fatec/TG-DRONE/ReconView/keras_model.h5", compile=False)

# Load the labels
class_names = open("/Users/joaovyctor/Documents/TG-Fatec/TG-DRONE/ReconView/labels.txt", "r").readlines()

# Abre a conexão com a câmera (0 para a câmera padrão)
camera = cv2.VideoCapture(0)

# Define as dimensões desejadas para a janela
window_width = 1280
window_height = 720

# Verifica se a câmera foi inicializada corretamente
if not camera.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

while True:
    # Captura a imagem da webcam.
    ret, image = camera.read()

    # Redimensiona a imagem bruta para as dimensões desejadas.
    resized_image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the model's input shape.
    image_input = np.asarray(resized_image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image_input = (image_input / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image_input)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Get the bounding box coordinates from your model's output
    # Assuming your model outputs x, y, width, and height
    x, y, w, h = prediction[0][1:5]  # Adjust this based on your model's output format

    # Scale the coordinates to match the resized image
    x *= 224
    y *= 224
    w *= 224
    h *= 224

    # Convert to integers
    x, y, w, h = int(x), int(y), int(w), int(h)

    # Draw a rectangle around the detected object
    cv2.rectangle(resized_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Mostra a imagem em uma janela redimensionada com o contorno.
    cv2.imshow("Webcam Image", cv2.resize(resized_image, (window_width, window_height)))

    # Escute o teclado para pressionamentos de tecla.
    keyboard_input = cv2.waitKey(1)

    # 27 é o código ASCII para a tecla Esc no teclado.
    if keyboard_input == 27:
        break

# Libera a câmera e fecha todas as janelas abertas.
camera.release()
cv2.destroyAllWindows()
