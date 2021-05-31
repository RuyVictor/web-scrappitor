# Components
from config.version import VERSION
from components.buttons import *
from components.textfields import *
from components.separators import *
from components.texts import *
from config.styles import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QGridLayout,
    QWidget,
    QHBoxLayout
)

# Functions
from functions.scrapping import (
    WebScrapping
)

main_window_stylesheet = """
    background-color: rgb(%(SECONDARY_COLOR)s);
""" % {'SECONDARY_COLOR': SECONDARY_COLOR}
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio")
        self.setFixedSize(640, 380)
        self.setStyleSheet(main_window_stylesheet)
        self.toggleButton = ToggleButton("  ACIONAR")
        self.textfieldURL = Textfield("https://www.google.com.br/")
        layout = QGridLayout()
        layout.setSpacing(14)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.addLayout(self.header(), 0, 0)
        layout.addWidget(Separator(3), 1, 0, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
        layout.addLayout(self.layoutTexfields(), 2, 0)
        layout.addWidget(self.toggleButton, 3, 0, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
        layout.addWidget(Separator(5), 4, 0, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
        layout.addWidget(Logsfield(""), 5, 0)
        self.setLayout(layout)

        # HANDLES
        self.toggleButton.clicked.connect(lambda: self.startScrapping())

    def startScrapping(self):
        self.scrapper = WebScrapping(self.textfieldURL.text())
        self.scrapper.start()

    # Sub layouts
    def header(self):
        layout = QHBoxLayout()
        label = Label("Versão: " + VERSION, PRIMARY_COLOR)
        label.setAlignment(Qt.AlignRight)

        layout.addWidget(Label(""))
        layout.addWidget(Title())
        layout.addWidget(label)
        return layout

    def layoutTexfields(self):
        layout = QGridLayout()
        layout.addWidget(Label("Insira a URL:", PRIMARY_COLOR), 0, 0)
        layout.addWidget(self.textfieldURL, 0, 1)
        return layout
