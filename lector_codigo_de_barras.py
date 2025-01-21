from PySide6.QtCore import QThread, Signal, QTimer
import cv2
from pyzbar.pyzbar import decode

class Capturadora_codigo_de_barra(QThread):
    codigo_escaneado = Signal(str)  # Señal para emitir el código escaneado

    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.scanned_codes = set()
        self.running = False

    def run(self):
        self.running = True
        print("Apunta la cámara al código de barras.")
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                print("No se pudo capturar el cuadro.")
                break

            # Decodifica los códigos de barras en el cuadro actual
            for barcode in decode(frame):
                code_data = barcode.data.decode('utf-8')
                code_type = barcode.type

                if code_data not in self.scanned_codes:
                    print(f"Código detectado: {code_data} (Tipo: {code_type})")
                    self.scanned_codes.add(code_data)
                    self.codigo_escaneado.emit(code_data)  # Emitir el código escaneado

                # Dibuja un rectángulo alrededor del código
                points = barcode.polygon
                if len(points) == 4:
                    pts = [(point.x, point.y) for point in points]
                    for i in range(len(pts)):
                        cv2.line(frame, pts[i], pts[(i + 1) % len(pts)], (0, 255, 0), 2)

            # Muestra el video en tiempo real
            cv2.imshow('Escáner de código de barras', frame)

            # Espera 1 ms y verifica si se debe detener
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def stop(self):
        self.running = False