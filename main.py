import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from MyGui import Ui_MainWindow
from MyEvent import MyEvents

if __name__=='__main__':
    app = QApplication()
    ui = Ui_MainWindow()
    view = QMainWindow()
    ui.setupUi(view)

    event = MyEvents(ui)
    
    view.show()
    sys.exit(app.exec_())