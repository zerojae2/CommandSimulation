import sys
import socket
from ultralytics import YOLO
import numpy as np
import cv2
import pyautogui
from PIL import Image
from asyncio.windows_events import NULL

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',6001))
model = YOLO("best.pt")

server.listen()

while True:
    client,address = server.accept()
    print('Connected')
    val = client.recv(1024).decode('utf-8')
    print(val)
    if val == 'click':
        while True:
            frame = pyautogui.screenshot()
            frame = np.array(frame)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            val = model(frame)

            for r in val:
                boxes = r.boxes.cpu().numpy()
                coord = boxes.xywhn
                conf = boxes.conf
                cls = boxes.cls

            str_arr = ""
            for i in coord:
                for j in i:
                    str_arr += str(j) + " "
            print(str_arr)

            client.send(str_arr.encode('utf-8'))
            
    client.close()
