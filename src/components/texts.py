from config.styles import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QLabel
)

def Title():
    label = QLabel("Web Scrapper")
    font = label.font()
    font.setPointSize(20)
    label.setFont(font)
    label.setStyleSheet("QLabel {color: rgb(%s); font-family: Nunito;}" % PRIMARY_COLOR)
    return label

def Label(text, color="black"):
    label = QLabel(text)
    font = label.font()
    font.setFamily("Roboto")
    font.setWeight(430)
    font.setPointSize(13)
    label.setFont(font)
    label.setStyleSheet("QLabel {color: rgb(%s);}" % PRIMARY_COLOR)
    return label
