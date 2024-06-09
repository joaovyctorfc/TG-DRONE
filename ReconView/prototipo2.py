from ultralytics import YOLO
import keyboard

modelo = YOLO('yolov8s.pt') # versoes, n ,s, m, l, x
modelo.predict(source='0', show=True)

def fechar_com_esc(event):
    if event.name == 'esc':
        modelo.close()  # Feche o modelo YOLO
        keyboard.unhook_all()  # Desconecte todos os ganchos de teclado
        quit()  # Encerre o programa

keyboard.on_press(fechar_com_esc)

# Mantenha o programa em execução
keyboard.wait('esc')
