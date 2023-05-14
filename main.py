import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton
from sqlalchemy import create_engine, text
from sqlalchemy.orm import create_session

engine = create_engine("postgresql+psycopg2://postgres:8909@localhost/school")
session = create_session(bind=engine)


class MainWindow(QMainWindow):     
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 180)
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        h2box = QtWidgets.QHBoxLayout()
        h3box = QtWidgets.QHBoxLayout()
        h4box = QtWidgets.QHBoxLayout()
        h5box = QtWidgets.QHBoxLayout()
        self.combox = QtWidgets.QComboBox()
        self.combox2 = QtWidgets.QComboBox()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        #классы
        self.combox.addItem("1")
        self.combox.addItem("2")
        self.combox.addItem("3")
        self.combox.addItem("4")
        self.combox.addItem("5")
        self.combox.addItem("6")
        self.combox.addItem("7")
        self.combox.addItem("8")
        self.combox.addItem("9")
        self.combox.addItem("10")
        self.combox.addItem("11")

        #индекс класса
        self.combox2.addItem("А")
        self.combox2.addItem("Б")
        self.combox2.addItem("В")
        self.combox2.addItem("Г")

        widget = QtWidgets.QWidget()
        self.line_edit = QtWidgets.QLineEdit()
        
        self.button = QPushButton("Выход")
        self.button2 = QPushButton("Добавить")
        lbl0 = QLabel("<center>Добавить ученика")
        lbl = QLabel("Добавить ФИО")
        lbl2 = QLabel("Выбрать класс")
        lbl3 = QLabel("Выбрать индекс класса")
        lbl4 = QPushButton("Добавить индекс класса")
        lbl4.setObjectName("index")

        self.button.clicked.connect(self.btn_exit)
        self.button2.clicked.connect(self.btn_add)
        
        
        #Последняя строка
        hbox.addWidget(self.button)
        hbox.addWidget(self.button2)

        #Строка 1
        h2box.addWidget(lbl)
        h2box.addWidget(self.line_edit)

        #Строка 2
        h3box.addWidget(lbl2)
        h3box.addWidget(self.combox)
        
        #Строка 3
        h4box.addWidget(lbl3)
        h4box.addWidget(self.combox2)
        
        #Строка индекс
        h5box.addWidget(lbl4)

        vbox.addWidget(lbl0)
        vbox.addLayout(h2box)
        vbox.addLayout(h3box)
        vbox.addLayout(h4box)
        vbox.addLayout(h5box)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


    def btn_exit(self):
        quit()

    def btn_add(self):

        
        sql_insert_student = text(f"INSERT INTO public.pupil(name, classes, class_index) VALUES ('{self.line_edit.text()}','{self.combox.currentText()}','{self.combox2.currentText()}')")

        session.execute(sql_insert_student)
        session.commit()
        session.close()

        
        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
with open("style.css", "r") as css:
    window.setStyleSheet(css.read())
window.show()
app.exec()
