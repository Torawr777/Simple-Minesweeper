from PyQt5.QtWidgets import QApplication
from MS_window import *

app = QApplication([])
window = MS_window()
window.show()
app.exec_()