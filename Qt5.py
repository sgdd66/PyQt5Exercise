#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

#测试1：生成一个简单窗口
def test1():
    app = QApplication(sys.argv)  # argv是命令行参数

    w = QWidget()
    w.resize(250, 150)
    w.move(0, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())  # app.exec_()说明应用进入主循环，应用结束后返回，之后由sys.exit（）清理垃圾并退出

#测试2：为窗口添加一个简单的图标
class Example2(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('2.jpg'))

        self.show()

def test2():

    app=QApplication(sys.argv)
    ex=Example2()
    sys.exit(app.exec_())

#测试3：显示提示文本
class Example3(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn=QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())#sizeHint()函数会返回一个推荐的按钮尺寸
        btn.move(50,50)


        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('2.jpg'))

        self.show()

def test3():
    app = QApplication(sys.argv)
    ex = Example3()
    sys.exit(app.exec_())

#测试4：点击按钮关闭窗口
class Example4(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


def test4():
    app = QApplication(sys.argv)
    ex = Example4()
    sys.exit(app.exec_())

if __name__=='__main__':
    test4()