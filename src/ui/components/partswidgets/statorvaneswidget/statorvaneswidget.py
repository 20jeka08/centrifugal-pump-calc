from src.api.statorvanescalc import StatorVanesCalc
from src.ui.components.partswidgets.statorvaneswidget.ui_statorvaneswidget import Ui_StatorVanesWidget
from PyQt5.QtWidgets import QWidget
from typing import Optional


class StatorVanesWidget(QWidget, Ui_StatorVanesWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.Q : Optional[float] = None
        self.H : Optional[float] = None
        self.n : Optional[float] = None
        self.i : Optional[int] = None

    def calc_statorvanes(self):

        st_v = StatorVanesCalc()
        st_v.Q = self.Q
        st_v.H = self.H
        st_v.n = self.n
        st_v.i = self.i

        self.volumeFlowRateLabel.setText(str(st_v.Q*3600))
        self.headOfPumpLabel.setText(str(st_v.H))
        self.rotationSpeedLabel.setText(str(st_v.n))
        self.numberOfStagesLabel.setText(str(st_v.i))


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = StatorVanesWidget()
    win.show()
    sys.exit(app.exec_())