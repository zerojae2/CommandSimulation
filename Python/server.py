import socket
from ultralytics import YOLO
import numpy as np
import cv2
import pyautogui

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 6001))
server.listen()

model = YOLO("best.pt")
print("Server started on 127.0.0.1:6001")

while True:
    client, address = server.accept()
    print(f'Connected: {address}')
    try:
        val = client.recv(1024).decode('utf-8').strip()
        print(f'Received: {val}')

        if val == 'click':
            while True:
                frame = pyautogui.screenshot()
                frame = np.array(frame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                results = model(frame)
                found_humen = False

                for r in results:
                    boxes = r.boxes.cpu().numpy()
                    classes = boxes.cls

                    for c in classes:
                        class_name = model.names[int(c)]
                        if class_name == "Humen":
                            found_humen = True
                            break  # 하나만 찾으면 됨

                if found_humen:
                    print("Sending: Humen")
                    client.send(b"Humen")
                else:
                    print("Sending: Nothing")
                    client.send(b"Nothing")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
