import cv2
import threading
import time
from pyzbar import pyzbar
from flask import Flask, Response, render_template

app = Flask(__name__)

# Inicializar la webcam
video_capture = cv2.VideoCapture(1)

# Variable para almacenar el contenido del QR
qr_data = ''


def read_qr_code():
    global video_capture, qr_data
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Leer los códigos QR en la imagen
        decoded_objects = pyzbar.decode(frame)

        # Actualizar el contenido del QR
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')

        time.sleep(0.1)

def generate_frames():
    global video_capture, qr_data
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Añadir el contenido del QR al vídeo
        if qr_data:
            cv2.putText(frame, qr_data, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/qr_data')
def get_qr_data(*args, **kwargs):
    global qr_data
    return qr_data


if __name__ == '__main__':
    # Iniciar hilo para leer códigos QR
    qr_thread = threading.Thread(target=read_qr_code, daemon=True)
    qr_thread.start()

    # Iniciar servidor Flask
    app.run(host='0.0.0.0', port=8000, threaded=True)
