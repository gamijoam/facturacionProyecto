import cv2
from pyzbar.pyzbar import decode

class Capturadora_codigo_de_barra:
    def __init__(self, code_data=None):
        # Inicializa la captura de video
        self.cap = cv2.VideoCapture(0)
        # Lista para almacenar códigos escaneados
        self.scanned_codes = set()
        self.codigo = code_data

    def mostrar_codigo(self, code_data, code_type):
        codigo = f"Código detectado: {code_data} (Tipo: {code_type})"
        return code_data

    def escanear_codigos(self):
        print("Apunta la cámara al código de barras. Presiona 'q' para salir.")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("No se pudo capturar el cuadro.")
                break

            # Decodifica los códigos de barras en el cuadro actual
            for barcode in decode(frame):
                code_data = barcode.data.decode('utf-8')  # Obtén los datos del código
                code_type = barcode.type  # Tipo del código (e.g., QR, CODE128)

                # Solo imprime y reproduce sonido si el código no ha sido escaneado antes
                if code_data not in self.scanned_codes:
                    print(self.mostrar_codigo(code_data, code_type))
                    self.scanned_codes.add(code_data)  # Agrega el código a la lista de escaneados

                # Dibuja un rectángulo alrededor del código
                points = barcode.polygon
                if len(points) == 4:
                    pts = [(point.x, point.y) for point in points]
                    for i in range(len(pts)):
                        cv2.line(frame, pts[i], pts[(i + 1) % len(pts)], (0, 255, 0), 2)

            # Muestra el video en tiempo real
            cv2.imshow('Escáner de código de barras', frame)

            # Presiona 'q' para salir
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        return code_data
        self.cap.release()
        cv2.destroyAllWindows()