from PyQt5.QtWidgets import QWidget
from src.ui.components.partswidgets.impellerwidget.ui_impellerwidget import Ui_ImpellerWidget
from src.api.impellercalc import ImpellerCalc


class ImpellerWidget(QWidget, Ui_ImpellerWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.imp = ImpellerCalc()
        self.calculatePushButton.clicked.connect(self.calc_impeller)

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

        if self.typePumpComboBox.currentText() == 'Single Stage, Single Entry':
            Eff = self.imp.EfficiencyRadialSingleStageSingeEntry()
            HydrEff = self.imp.HydraulicEfficiencyRadialPumpSingleStage()
            C_kr = 1000.0
            double_entry = False
        elif self.typePumpComboBox.currentText() == 'Single Stage, Double Entry':
            Eff = self.imp.EfficiencyRadialSingleStageDoubleEntry()
            HydrEff = self.imp.HydraulicEfficiencyRadialPumpSingleStage()
            C_kr = 1200.0
            double_entry = True
        else:
            Eff = self.imp.EfficiencyRadialMultistageSingleEntry()
            HydrEff = self.imp.HydraulicEfficiencyRadialPumpMultistage()
            C_kr = 800.0
            double_entry = False

        Pmax = self.imp.Pmax(Efficiency=Eff)
        s_sf = self.shaftSafetyFactorDoubleSpinBox.value()
        d0 = self.imp.shaftD(Pmax=Pmax, factorSafety=s_sf)
        self.d0Label.setText(str(d0))
        D0 = self.imp.D1LambdaMethod(shaftD=d0)
        self.D0Label.setText(str(round(D0, 2)))
        L = self.imp.L(D2=D2)
        self.LLabel.setText(str(round(L, 2)))

        volume_efficiency = self.imp.VolumeEffEstimation()
        c1m = self.imp.c1m(D1=D0, shaftD=d0, volumeEfficiency=volume_efficiency)
        u1h = self.imp.u1(d0)
        u1s = self.imp.u1(D0)
        e1 = self.imp.bladeThickness(D2)
        Z = self.bladesNumberSpinBox.value()

        beta1s = self.imp.inletBladeAngle(c1m=c1m, u1=u1s, D1=D0, Z=Z, e1=e1, i=0.0)
        beta1h = self.imp.inletBladeAngle(c1m=c1m, u1=u1h, D1=D0, Z=Z, e1=e1, i=0.0)
        beta2 = self.beta2DoubleSpinBox.value()

        self.Beta1sLabel.setText(str(beta1s))
        self.Beta1hLabel.setText(str(beta1h))
        self.Beta2Label.setText(str(beta2))

        omega_blade = self.imp.omegaBlade(Z=Z)
        self.omegaBladeLabel.setText(str(round(omega_blade, 2)))

        e1 = self.imp.bladeThickness(D2=D2)
        self.thiknessLabel.setText(str(e1))

        self.cavitationCoefficientLabel.setText(str(C_kr))
        dh = self.imp.cavitationHead(C_kr=C_kr, doubleEntry=double_entry)
        self.cavitationValueLabel.setText(str(dh))

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = ImpellerWidget()
    win.show()
    sys.exit(app.exec_())
