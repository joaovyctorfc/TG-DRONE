import cv2

# Abre a conexão com a câmera (0 para a câmera padrão)
cap = cv2.VideoCapture(0)

# Verifica se a câmera foi inicializada corretamente
if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

while True:
    # Captura um quadro da câmera
    ret, frame = cap.read()

    # Verifica se o quadro foi capturado corretamente
    if not ret:
        print("Erro ao capturar o quadro.")
        break

    # Mostra o quadro em uma janela
    cv2.imshow("Webcam", frame)

    # Escuta o teclado para sair (pressionando a tecla 'q')
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
