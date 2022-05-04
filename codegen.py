import os


class CodeGen:
    def __init__(self):
        self._command_ui = 'pyuic5 -x .\\src\\ui\\components\\partswidgets\\impellerwidget\\impellerwidget.ui -o ' \
                        '.\\src\\ui\\components\\partswidgets\\impellerwidget\\ui_impellerwidget.py'

        self._command_qcc = 'pyrcc5 .\\src\\ui\\styles\\impellerwidget.qrc -o ' \
                            '.\\src\\ui\\impellerwidget_rc.py'

        self._command_qcc_main = 'pyrcc5 .\\src\\ui\\styles\\mainwidget.qrc -o ' \
                            '.\\src\\ui\\mainwidget_rc.py'

        self._command_ui_main = 'pyuic5 -x .\\src\\ui\\mainwidget.ui -o .\\src\\ui\\ui_mainwidget.py'

    def generate(self):
        os.system(self._command_ui)
        os.system(self._command_qcc)
        os.system(self._command_ui_main)
        os.system(self._command_qcc_main)


if __name__ == '__main__':
    gen = CodeGen()
    gen.generate()
