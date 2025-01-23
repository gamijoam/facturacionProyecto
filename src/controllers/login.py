from PySide6 import QtWidgets
from src.controllers.panel_de_control import panel_de_control
from src.view.PY.ui_login import Ui_Form


def login(self):
    ui_login = Ui_Form()  # Crea una instancia de la interfaz de inicio de sesión.
    ui_login.setupUi(self)
    ui_login.pushButton.clicked.connect(lambda:cerrar_ventana(self))

def cerrar_ventana(self):
    self.close()
    panel_de_control(self)