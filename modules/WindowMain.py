import os
from PyQt5 import QtGui
from modules.ui_main import *
import modules.blur

os.environ["QT_FONT_DPI"] = "96"


class WindowMain(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sideMenuExpanded = False
        self.dragPos = QPoint()
        self.GLOBAL_STATE = False
        self.FadeInAnimation = QPropertyAnimation(self, b"windowOpacity")
        WIcon = QtGui.QIcon()
        WIcon.addPixmap(QtGui.QPixmap("resources/ning-white-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(WIcon)
        # Minimize
        self.ui.MinimizeBtn.clicked.connect(lambda: self.showMinimized())
        # Maximize/Restore
        self.ui.MaximizeBtn.clicked.connect(lambda: self.maximize_restore())
        # Close Application
        self.ui.CloseBtn.clicked.connect(lambda: self.CloseWindow())
        # Move Window
        self.ui.title.mouseMoveEvent = self.moveWindow
        # expand sidemenu
        self.ui.icon.clicked.connect(self.toggleBox)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def ShowWindow(self, enableBlur):
        self.setWindowOpacity(0)
        self.show()
        self.WindowFade(0, 1)
        if enableBlur:
            modules.blur.windowblur(self.windowTitle())
    def moveWindow(self, event):
        # if maximized change to normal
        if self.GLOBAL_STATE:
            self.maximize_restore()
            self.move(event.globalPos() - QPoint(500, 15))
        # move window
        if event.buttons() == Qt.LeftButton:
            if self.dragPos.isNull():
                self.dragPos = event.globalPos()
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def maximize_restore(self):
        if not self.GLOBAL_STATE:
            self.showMaximized()
            self.GLOBAL_STATE = True
            self.ui.MaximizeBtn.setToolTip("Restore")
            self.ui.MaximizeBtn.setIcon(QIcon(u"resources/ic_restore.png"))
        else:
            self.GLOBAL_STATE = False
            self.showNormal()
            self.ui.MaximizeBtn.setToolTip("Maximize")
            self.ui.MaximizeBtn.setIcon(QIcon("resources/ic_maximize.png"))

    def toggleBox(self):
        self.ui.left_box = QPropertyAnimation(self.ui.sidemenu, b"minimumWidth")
        self.ui.left_box.setDuration(250)
        self.ui.left_box.setEasingCurve(QEasingCurve.OutCubic)
        if self.sideMenuExpanded:
            self.ui.left_box.setStartValue(240)
            self.ui.left_box.setEndValue(50)
        else:
            self.ui.left_box.setStartValue(50)
            self.ui.left_box.setEndValue(240)
        self.ui.left_box.start()
        self.sideMenuExpanded = not self.sideMenuExpanded

    # Window FadeIn/FadeOut
    def WindowFade(self, s, e):
        self.FadeInAnimation.setDuration(150)
        self.FadeInAnimation.setStartValue(s)
        self.FadeInAnimation.setEndValue(e)
        self.FadeInAnimation.start()

    def CloseWindow(self):
        self.WindowFade(1, 0)
        self.FadeInAnimation.finished.connect(lambda: self.close())
