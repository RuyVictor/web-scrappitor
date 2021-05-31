from config.styles import *
from PyQt5.QtWidgets import (
    QFrame
)

separator_stylesheet = """
    .QFrame {
        background-color: rgb(%(PRIMARY_COLOR)s);
        border: 1px solid rgb(%(PRIMARY_COLOR)s);
    }
""" % {'PRIMARY_COLOR': PRIMARY_COLOR}

def Separator(width=6):
    separator = QFrame()
    separator.setFrameShape(QFrame.HLine)
    separator.setFrameShadow(QFrame.Raised)
    separator.setStyleSheet(separator_stylesheet)
    separator.setFixedSize(separator.geometry().width() / width, 2)
    return separator