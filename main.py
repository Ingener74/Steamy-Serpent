# encoding: utf8
import sys
from PySide.QtCore import QStateMachine, QState, SIGNAL
from PySide.QtGui import QApplication, QWidget
from res import Ui_SteamySerpent


class SteamySerpent(QWidget, Ui_SteamySerpent):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        machine = QStateMachine()

        s11 = QState()
        s11.assignProperty(self.ChangeState, 'text', 'State 11')

        s12 = QState()
        s12.assignProperty(self.ChangeState, 'text', 'State 12')

        s13 = QState()
        s13.assignProperty(self.ChangeState, 'text', 'State 13')

        # s11.entered.connect(self.s11entered)

        s11.addTransition(self.ChangeState.clicked, s12)
        s12.addTransition(self.ChangeState.clicked, s13)
        s13.addTransition(self.ChangeState.clicked, s11)

        machine.addState(s11)
        machine.addState(s12)
        machine.addState(s13)

        machine.setInitialState(s11)

        machine.start()

    def s11entered(self):
        print 's11 entered'


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = SteamySerpent()
    window.show()

    sys.exit(app.exec_())