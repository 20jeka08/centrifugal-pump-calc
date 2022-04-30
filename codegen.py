import os


class CodeGen:
    def __init__(self):
        self._command_ui = 'pyuic5 -x .\\src\\ui\\components\\partswidgets\\impellerwidget\\impellerwidget.ui -o ' \
                        '.\\src\\ui\\components\\partswidgets\\impellerwidget\\ui_impellerwidget.py'

        self._command_qcc = 'pyrcc5 .\\src\\ui\\styles\\impellerwidget.qrc -o ' \
                            '.\\src\\ui\\components\\partswidgets\\impellerwidget\\impellerwidget_rc.py'

    def generate(self):
        os.system(self._command_ui)
        os.system(self._command_qcc)


if __name__ == '__main__':
    gen = CodeGen()
    gen.generate()
