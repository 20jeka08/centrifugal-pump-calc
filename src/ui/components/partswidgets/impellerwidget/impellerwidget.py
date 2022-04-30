from PyQt5.QtWidgets import QWidget
from src.ui.components.partswidgets.impellerwidget.ui_impellerwidget import Ui_ImpellerWidget
from src.api.impellercalc import ImpellerCalc


class ImpellerWidget(QWidget, Ui_ImpellerWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.imp = None
        self.calculatePushButton.clicked.connect(self.calc_impeller)

    def set_impeller(self, impeller: ImpellerCalc):
        self.imp = impeller

    def calc_impeller(self):

        self.imp.Q = float(self.volumeFlowRateLineEdit.text()) / 3600
        self.imp.H = float(self.headPumpLineEdit.text())
        self.imp.n = float(self.rotationSpeedLineEdit.text())
        self.imp.i = 1

        self.nsLabel.setText(str(self.imp.ns))
        self.nqLabel.setText(str(self.imp.nq))


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = ImpellerWidget()
    imp = ImpellerCalc()
    win.set_impeller(impeller=imp)
    win.show()
    sys.exit(app.exec_())
