import qtawesome as qta
from config.styles import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QPushButton,
    QGraphicsDropShadowEffect
)

button_stylesheet = """
    QPushButton {
        background-color: rgb(%(PRIMARY_COLOR)s);
        color: rgb(%(SECONDARY_COLOR)s);
        border-radius: 3px;
        padding: 10px 50px;
    }
    QPushButton::hover {
        color: rgb(%(SECONDARY_COLOR)s);
    }
    QPushButton::pressed {
        background-color: rgba(%(PRIMARY_COLOR)s, 180);
    }
""" % {'PRIMARY_COLOR': PRIMARY_COLOR, 'SECONDARY_COLOR': SECONDARY_COLOR}
timer = QtCore.QTimer()

def ToggleButton(text):
    icon_anim = qta.IconWidget()
    icon = qta.icon("fa5s.biohazard", color="#e6e6e6", scale_factor=1.2)
    spin_icon = qta.icon('mdi.loading', color="#e6e6e6", animation=qta.Spin(icon_anim), scale_factor=1.5)
    button = QPushButton(icon, text)
    font = button.font()
    font.setFamily('Roboto')
    font.setPointSize(13)
    button.setFont(font)
    button.setStyleSheet(button_stylesheet)
    effect = QGraphicsDropShadowEffect(button, blurRadius=50)
    effect.setColor(QColor(SECONDARY_COLOR))
    effect.setOffset(0, 0)
    button.setGraphicsEffect(effect)
    button.clicked.connect(lambda: button.setIcon(spin_icon))
    return button
