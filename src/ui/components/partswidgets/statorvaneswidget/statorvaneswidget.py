from src.api.statorvanescalc import StatorVanesCalc
from src.ui.components.partswidgets.statorvaneswidget.ui_statorvaneswidget import Ui_StatorVanesWidget
from PyQt5.QtWidgets import QWidget
from typing import Optional


class StatorVanesWidget(QWidget, Ui_StatorVanesWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.Q: Optional[float] = None
        self.H: Optional[float] = None
        self.n: Optional[float] = None
        self.i: Optional[int] = None

        self.ns: Optional[float] = None
        self.nq: Optional[float] = None
        self.D2: Optional[float] = None
        self.b2: Optional[float] = None
        self.d0: Optional[float] = None
        self.D0: Optional[float] = None
        self.hydraulicEff: Optional[float] = None
        self.Z_imp: Optional[int] = None

    def calc_statorvanes(self):

        st_v = StatorVanesCalc()
        st_v.Q = self.Q
        st_v.H = self.H
        st_v.n = self.n
        st_v.i = self.i
        st_v.ns = self.ns
        st_v.nq = self.nq
        st_v.Hi = st_v.H/st_v.i

        self.volumeFlowRateLabel.setText(str(st_v.Q*3600))
        self.headOfPumpLabel.setText(str(st_v.H))
        self.rotationSpeedLabel.setText(str(st_v.n))
        self.numberOfStagesLabel.setText(str(st_v.i))
        self.nsLabel.setText(str(st_v.ns))
        self.nqLabel.setText(str(st_v.nq))

        D3_D2 = st_v.D3_D2()
        D3 = round(st_v.D3(D2=self.D2, D3toD2=D3_D2), 2)
        self.D3Label.setText(str(D3))

        b3_b2 = self.widthRatiob3b2DoubleSpinBox.value()
        b3 = round(b3_b2*self.b2, 2)
        self.b3Label.setText(str(b3))

        D4_D2 = st_v.D4_D2(priority=self.radialDimensionRatioDoubleSpinBox.value())
        D4 = round(st_v.D4(D4toD2=D4_D2, D2=self.D2), 2)
        self.D4Label.setText(str(D4))

        vol_eff = st_v.VolumeEffEstimation()
        c1m = st_v.c1m(D1=self.D0, shaftD=self.d0, volumeEfficiency=vol_eff)
        c6m = st_v.c6m(c1m=c1m)
        D6 = self.D0
        b5 = round(st_v.b6(c6m=c6m, D6=D6), 2)

        self.b5Label.setText(str(b5))

        D5 = round(D4 + (b5 + b3) / 2.0, 2)
        self.D5Label.setText(str(D5))


        c3m = st_v.c3m(D3=D3, b3=b3)

        u2 = st_v.u2(D2=self.D2)
        c2u = st_v.c2u(hydraulicEff=self.hydraulicEff, u2=u2)
        c3u = st_v.c3u(D2=self.D2, D3=D3, c2u=c2u)
        alpha3 = round(st_v.alpha3(c3m=c3m, c3u=c3u), 2)
        self.beta3Label.setText(str(alpha3))

        alpha4 = round(st_v.alpha4(alpha3=alpha3, D4toD2=D4_D2), 2)
        self.beta4Label.setText(str(alpha4))

        alpha5 = round(st_v.alpha5(alpha4=alpha4, b3=b3, b6=b5), 2)
        self.beta5Label.setText(str(alpha5))
        self.beta6Label.setText(str(st_v.alpha6()))

        if self.Z_imp < 5:
            Z3 = 7
        elif self.Z_imp == 5:
            Z3 = 8
        elif self.Z_imp == 6:
            Z3 = 10
        elif self.Z_imp == 7:
            Z3 = 11
        elif 7 < self.Z_imp < 11:
            Z3 = 11
        elif 11 <= self.Z_imp < 13:
            Z3 = 13
        elif self.Z_imp > 13:
            Z3 = 15

        self.numberOfBladesLabel.setText(str(Z3))

        e3 = round(0.0125 * self.D2, 2)
        self.thicknessLabel.setText(str(e3))


















if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = StatorVanesWidget()
    win.show()
    sys.exit(app.exec_())