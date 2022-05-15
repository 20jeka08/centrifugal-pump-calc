from src.api.statorvanescalc import StatorVanesCalc
from src.ui.components.partswidgets.statorvaneswidget.ui_statorvaneswidget import Ui_StatorVanesWidget
from PyQt5.QtWidgets import QWidget


class StatorVanesWidget(QWidget, Ui_StatorVanesWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = StatorVanesWidget()
    win.show()
    sys.exit(app.exec_())