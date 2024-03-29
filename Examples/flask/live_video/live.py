import cv2
import numpy as np

vid = cv2.VideoCapture(0)
# vid = cv2.VideoCapture(url)

def gen_one_frame():
    while True:
        ret, frame = vid.read()

        if frame is not None:
            yield frame
        else:
            print("Frame is None")
            break

def gen_surveillance():
    for frame in gen_one_frame():
        ret, jpeg = cv2.imencode('.jpeg', frame)

        yield ( b'--frame\r\n'
        b'Content-Type:image/jpeg\r\n'
        b'Content-Length: ' + f"{jpeg.size}".encode() + b'\r\n'
        b'\r\n' + jpeg.tobytes() + b'\r\n')