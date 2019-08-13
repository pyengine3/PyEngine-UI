import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QSpacerItem, QLineEdit, QCheckBox, QSpinBox, QPushButton, QFileDialog

from pyengine_ui.Core.Utils import get_properties
from pyengine_ui.Core.Widgets import Label


class PropertiesWidget(QWidget):
    def __init__(self, obj):
        super(PropertiesWidget, self).__init__()
        self.obj = obj
        self.grid = QGridLayout()
        self.grid.setSizeConstraint(self.grid.SetMinAndMaxSize)

        title = Label("Propriété : "+self.obj.type_, 16)
        title.setMaximumHeight(80)
        title.setMinimumHeight(80)
        title.setAlignment(Qt.AlignHCenter)
        self.grid.addWidget(title, 0, 0, 1, 2)

        nb = 1
        for n, t in get_properties(self.obj.type_).items():
            label = Label(n, 12)
            label.setMaximumHeight(50)
            label.setMinimumHeight(50)
            label.setAlignment(Qt.AlignCenter)
            self.grid.addWidget(label, nb, 0)

            if t == "str":
                widget = QLineEdit()
                widget.setText(self.obj.properties.get(n, ""))
                widget.textChanged.connect(lambda text="", prop=n: self.set_text_for(text, prop))
            elif t == "bool":
                widget = QCheckBox()
                if self.obj.properties.get(n, False):
                    widget.setChecked(True)
                widget.stateChanged.connect(lambda state=0, prop=n: self.set_bool_for(state, prop))
            elif t == "int":
                widget = QSpinBox()
                widget.setMaximum(3000)
                widget.setValue(self.obj.properties.get(n, 0))
                widget.valueChanged.connect(lambda value=0, prop=n: self.set_int_for(value, prop))
            elif t == "file":
                widget = QPushButton("Selectionner")
                widget.clicked.connect(lambda checked=False, prop=n: self.set_file_for(prop))
            else:
                raise TypeError("Unknown type for properties : "+t)
            self.grid.addWidget(widget, nb, 1)

            nb += 1

        end_spacer = QSpacerItem(20, 2000)
        self.grid.addItem(end_spacer, nb, 0)

        for i in range(0, 2):
            self.grid.setColumnStretch(i, 1)

        self.setLayout(self.grid)

    def set_text_for(self, text, prop):
        self.obj.set_property(prop, text)

    def set_bool_for(self, state, prop):
        self.obj.set_property(prop, bool(state))

    def set_int_for(self, value, prop):
        self.obj.set_property(prop, value)

    def set_file_for(self, prop):
        directory = os.environ.get('HOME', os.environ.get('USERPROFILE', os.path.dirname(__file__)))
        self.obj.set_property(prop, QFileDialog.getOpenFileName(self, "Fichier : "+prop, directory))

