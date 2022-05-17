from PyQt5.QtWidgets import QWidget
from src.ui.ui_mainwidget import Ui_MainWidget


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.calculatePushButton.clicked.connect(self.calc_all)

    def calc_all(self):
        self.impellerTab.calc_impeller()
        self.statorVanesTab.Q = self.impellerTab.imp.Q
        self.statorVanesTab.H = float(self.impellerTab.headLabel.text())
        self.statorVanesTab.n = self.impellerTab.imp.n
        self.statorVanesTab.i = self.impellerTab.imp.i
        self.statorVanesTab.ns = self.impellerTab.imp.ns
        self.statorVanesTab.nq = self.impellerTab.imp.nq
        self.statorVanesTab.D2 = float(self.impellerTab.d2Label.text())
        self.statorVanesTab.b2 = float(self.impellerTab.b2Label.text())
        self.statorVanesTab.D0 = float(self.impellerTab.D0Label.text())
        self.statorVanesTab.d0 = float(self.impellerTab.d0Label.text())
        self.statorVanesTab.c2u = self.impellerTab.imp.c2u
        self.statorVanesTab.hydraulicEff = self.impellerTab.hydraulicEff
        self.statorVanesTab.Z_imp = self.impellerTab.bladesNumberSpinBox.value()
        self.statorVanesTab.calc_statorvanes()







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = MainWidget()
    win.show()
    sys.exit(app.exec_())

