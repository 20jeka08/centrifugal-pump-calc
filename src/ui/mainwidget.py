from PyQt5.QtWidgets import QWidget
from src.ui.ui_mainwidget import Ui_MainWidget
from src.ui.components.partswidgets.impellerwidget.impellerwidget import ImpellerWidget


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = MainWidget()
    win.show()
    sys.exit(app.exec_())

