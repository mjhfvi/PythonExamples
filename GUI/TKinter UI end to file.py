if __name__=="__main__":
    import sys
    from PyQt5.QtGui import QIcon
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.setWindowIcon(QIcon('web.png'))#Add icon icon, if there is no picture, there is no such sentence
    widget.show()
    sys.exit(app.exec_())