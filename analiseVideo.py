# import requests
# import shutil
# from ultralytics import YOLO
# import cv2

# def baixar_video_do_firebase(url, destino):
#     try:
#         # Faz o download do vídeo
#         resposta = requests.get(url)
#         # Verifica se a solicitação foi bem-sucedida
#         if resposta.status_code == 200:
#             # Abre o arquivo de destino em modo de escrita binária
#             with open(destino, 'wb') as arquivo:
#                 # Escreve os dados do vídeo no arquivo
#                 arquivo.write(resposta.content)
#             print("Download concluído com sucesso.")
#         else:
#             print("Falha ao baixar o vídeo. Status code:", resposta.status_code)
#     except Exception as e:
#         print("Ocorreu um erro:", e)

# # URL do vídeo no Firebase Storage
# url_do_video = "https://firebasestorage.googleapis.com/v0/b/reconview-1410a.appspot.com/o/your_type_here%2FWhatsApp%20Video%202024-05-09%20at%2018.27.55.mp4?alt=media&token=f12ce56f-02ec-4f2d-8aa8-f2d096ed428f"
# # Caminho de destino onde o vídeo será salvo
# caminho_de_destino = "C:\\Users\\Cliente\\Music\\GitHub\\TG-DRONE\\videos\\downloads\\"

# # Chamada da função para baixar o vídeo
# baixar_video_do_firebase(url_do_video, caminho_de_destino)

# # Configure the tracking parameters and run the tracker
# modelo = YOLO('yolov8n.pt')

# videoPath = r"C:\Users\Cliente\Music\GitHub\TG-DRONE\cars.mp4"
# resultado = modelo.predict(source=videoPath, conf=0.5, iou=0.5, show=True)

