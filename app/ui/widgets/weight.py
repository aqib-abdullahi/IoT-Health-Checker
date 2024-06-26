#!/usr/bin/env python3
"""weight input window"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import (QWidget,
                             QSpinBox,
                             QVBoxLayout,
                             QHBoxLayout,
                             QApplication,
                             QPushButton,
                             QFormLayout
                             )


class Weight(QWidget):
    """weight option to set
    """
    def __init__(self):
        """initializes the window"""
        super().__init__()

        self.setWindowTitle("Input weight")
        self.setGeometry(0, 0, 600, 400)
        self.setMinimumWidth(400)
        self.setMinimumHeight(60)
        self.setMaximumSize(700, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.form = QFormLayout()
        # dropdown list of gender
        self.weight = QSpinBox(minimum=1, maximum=500, suffix='  Kg')

        # Spinbox style (dropdown list styling)
        self.weight.setStyleSheet(" font-size: 12px; font-weight: bold; "
                              "qproperty-alignment: AlignCenter; font-family: Arial;")
        self.weight.setFixedSize(150,20)

        self.form.addRow("Weight:   ", self.weight)
        self.form.setFormAlignment(Qt.AlignmentFlag.AlignCenter)

        # adds name edit to layout
        layout.addLayout(self.form)

        # buttons (backward and forward)
        self.nav_buttons = QHBoxLayout()
        self.nav_buttons.addStretch(3)
        self.back_button = QPushButton("< Back")
        self.next_button = QPushButton("Next >")
        self.nav_buttons.addWidget(self.back_button)
        self.nav_buttons.addWidget(self.next_button)

        # style buttons
        self.next_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                                  "qproperty-alignment: AlignLeft; font-family: Arial;")
        self.back_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                                  "qproperty-alignment: AlignLeft; font-family: Arial;")

        # adds button to layout
        layout.addLayout(self.nav_buttons)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

        self.user_weight = None
        self.prev_window = None
        self.next_information_window = None
        self.last_information_window  = None

    def user_weight_input(self):
        """holds and print user's input"""
        self.user_weight = self.weight.text()
        print("Weight: ", self.user_weight)
        return self.user_weight

    def set_gender_previous_window(self, prev_window):
        """set devices window
        """
        self.prev_window = prev_window
        self.back_button.clicked.connect(self.show_gender_previous_window)

    def show_gender_previous_window(self):
        """shows previous window"""
        self.close()
        self.prev_window.show()

    def set_information_next_window(self, next_information_window, last_information_window):
        """sets the gender window"""
        self.next_information_window = next_information_window
        self.last_information_window = last_information_window
        self.next_button.clicked.connect(self.show_information_next_window)

    def show_information_next_window(self):
        """show the date window as next"""
        self.close()
        self.last_information_window.update_weight(self.user_weight_input())
        self.next_information_window.show()