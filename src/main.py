import sys
from views.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("assets/fonts/Nunito-Light.ttf")
    QFontDatabase.addApplicationFont("assets/fonts/Nunito-Regular.ttf")
    QFontDatabase.addApplicationFont("assets/fonts/Nunito-SemiBold.ttf")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
