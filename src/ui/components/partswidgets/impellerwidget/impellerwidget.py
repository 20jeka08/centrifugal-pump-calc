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

        self.imp.Q = self.volumeFlowRateDoubleSpinBox.value() / 3600
        self.imp.H = self.headPumpDoubleSpinBox.value()
        self.imp.n = self.rotationSpeedDoubleSpinBox.value()
        self.imp.i = self.numberStagesSpinBox.value()

        self.nsLabel.setText(str(self.imp.ns))
        self.nqLabel.setText(str(self.imp.nq))
        D2 = self.imp.D2(psi=self.imp.psi(ft=self.hQCurveDoubleSpinBox.value()))
        self.d2Label.setText(str(D2))
        b2 = self.imp.b2(D2=D2)
        self.b2Label.setText(str(b2))


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = ImpellerWidget()
    imp = ImpellerCalc()
    win.set_impeller(impeller=imp)
    win.show()
    sys.exit(app.exec_())
