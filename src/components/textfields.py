from config.styles import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QLineEdit,
    QPlainTextEdit,
    QGraphicsDropShadowEffect
)

textfield_stylesheet = """
    QLineEdit {
        background-color: rgba(255, 255, 255, 10);
        border: 1px solid rgb(%(PRIMARY_COLOR)s);
        border-radius: 4px;
        color: #e6e6e6;
        padding: 5px 10px;
    }
""" % {'PRIMARY_COLOR': PRIMARY_COLOR}

logsfield_stylesheet = """
    QPlainTextEdit {
        background-color: rgba(255, 255, 255, 10);
        border: 1px solid rgb(%(PRIMARY_COLOR)s);
        border-radius: 4px;
        color: #e6e6e6;
        padding: 5px 10px;
    }
""" % {'PRIMARY_COLOR': PRIMARY_COLOR}

def Textfield(placeholder):
    textfield = QLineEdit()
    font = textfield.font()
    font.setPointSize(11)
    textfield.setFont(font)
    textfield.setStyleSheet(textfield_stylesheet)
    effect = QGraphicsDropShadowEffect(textfield, blurRadius=20)
    effect.setColor(QColor(SECONDARY_COLOR))
    effect.setOffset(0, 0)
    textfield.setGraphicsEffect(effect)
    textfield.setPlaceholderText(placeholder)
    return textfield

def Logsfield(logs):
    logsfield = QPlainTextEdit(logs)
    font = logsfield.font()
    font.setPointSize(11)
    logsfield.setFont(font)
    logsfield.setStyleSheet(logsfield_stylesheet)
    effect = QGraphicsDropShadowEffect(logsfield, blurRadius=20)
    effect.setColor(QColor(SECONDARY_COLOR))
    effect.setOffset(0, 0)
    logsfield.setGraphicsEffect(effect)
    logsfield.setReadOnly(True)
    return logsfield