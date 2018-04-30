import sys

import pkg_resources

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence, QColor
from PyQt5.QtWidgets import (QAction, QApplication, QDesktopWidget, QDialog, QFileDialog,
                             QHBoxLayout, QLabel, QMainWindow, QToolBar, QVBoxLayout, QWidget,
                             QShortcut, QPushButton, QFrame, qApp)


class Template(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(Template, self).__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle('Template')
        window_icon = pkg_resources.resource_filename('demo-qt-inspector.images',
                                                      'ic_insert_drive_file_black_48dp_1x.png')
        self.setWindowIcon(QIcon(window_icon))
        self.initUI()
        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)

        print(qApp.styleSheet())

        with open("theme.qss", mode="r") as theme_file:
            qApp.setStyleSheet(theme_file.read())

        self.menu_bar = self.menuBar()
        self.about_dialog = AboutDialog()

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready')

        self.file_menu()
        self.help_menu()


    def file_menu(self):
        """Create a file submenu with an Open File item that opens a file dialog."""
        self.file_sub_menu = self.menu_bar.addMenu('File')

        self.open_action = QAction('Open File', self)
        self.open_action.setStatusTip('Open a file into Template.')
        self.open_action.setShortcut('CTRL+O')

        self.exit_action = QAction('Exit Application', self)
        self.exit_action.setStatusTip('Exit the application.')
        self.exit_action.setShortcut('CTRL+Q')
        self.exit_action.triggered.connect(lambda: QApplication.quit())

        self.file_sub_menu.addAction(self.open_action)
        self.file_sub_menu.addAction(self.exit_action)

    def help_menu(self):
        """Create a help submenu with an About item tha opens an about dialog."""
        self.help_sub_menu = self.menu_bar.addMenu('Help')

        self.about_action = QAction('About', self)
        self.about_action.setStatusTip('About the application.')
        self.about_action.setShortcut('CTRL+H')
        self.about_action.triggered.connect(lambda: self.about_dialog.exec_())

        self.help_sub_menu.addAction(self.about_action)


    def initUI(self):

        self.color = QColor(0, 0, 0)
        self.square = QFrame(self)
        self.square.setGeometry(150, 60, 150, 150)
        self.square.setStyleSheet("QWidget {{ background-color: {0} }}".format(self.color.name()))

        red_button = QPushButton('Red', self)
        red_button.setCheckable(True)
        red_button.move(10, 60)
        red_button.setObjectName("RedButton")

        red_button.clicked[bool].connect(self.setColor)

        green_button = QPushButton('Green', self)
        green_button.setCheckable(True)
        green_button.move(10, 120)
        green_button.setObjectName("GreenButton")

        green_button.clicked[bool].connect(self.setColor)

        blue_button = QPushButton('Blue', self)
        blue_button.setCheckable(True)
        blue_button.move(10, 180)
        blue_button.setObjectName("BlueButton")

        blue_button.clicked[bool].connect(self.setColor)


    def setColor(self, pressed):
        val = 255 if pressed else 0
        source = self.sender()

        if source.text() == "Red":
            self.color.setRed(val)
        elif source.text() == "Green":
            self.color.setGreen(val)
        else:
            self.color.setBlue(val)

        self.square.setStyleSheet("QFrame {{ background-color: {0} }}".format(self.color.name()))


class AboutDialog(QDialog):
    """Create the necessary elements to show helpful text in a dialog."""

    def __init__(self, parent=None):
        """Display a dialog that shows application information."""
        super(AboutDialog, self).__init__(parent)

        self.setWindowTitle('About')
        help_icon = pkg_resources.resource_filename('demo-qt-inspector.images',
                                                    'ic_help_black_48dp_1x.png')
        self.setWindowIcon(QIcon(help_icon))
        self.resize(300, 200)

        author = QLabel('demo_qt_inspector')
        author.setAlignment(Qt.AlignCenter)

        icons = QLabel('Material design icons created by Google')
        icons.setAlignment(Qt.AlignCenter)

        github = QLabel('GitHub: williamjamir')
        github.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignVCenter)

        self.layout.addWidget(author)
        self.layout.addWidget(icons)
        self.layout.addWidget(github)

        self.setLayout(self.layout)


class ConnectStyleSheetInspector(object):

    def __init__(self, main_window, shortcut):
        self.shortcut = shortcut
        self.main_window = main_window
        shortcut_ = QShortcut(self.shortcut, main_window)
        shortcut_.setContext(Qt.ApplicationShortcut)

        def ShowStyleSheetEditor():
            style_sheet_inspector_class = GetStyleSheetInspectorClass()
            style_sheet_inspector = [
                c for c in self.main_window.children() if
                isinstance(c, style_sheet_inspector_class)]
            if style_sheet_inspector:
                style_sheet_inspector = style_sheet_inspector[0]
            else:
                style_sheet_inspector = style_sheet_inspector_class(self.main_window)
                style_sheet_inspector.setFixedSize(800, 600)
            style_sheet_inspector.show()

        shortcut_.activated.connect(ShowStyleSheetEditor)


def GetStyleSheetInspectorClass():
    """
    Indirection mostly to simplify tests.
    """
    try:
        from qt_style_sheet_inspector import StyleSheetInspector
    except ImportError as error:
        msg = 'You need to Install qt_style_sheet_inspector.'
        raise RuntimeError(msg)
    return StyleSheetInspector


def main():
    application = QApplication(sys.argv)
    window = Template()

    ConnectStyleSheetInspector(main_window=window,
                               shortcut=QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_F12))
    desktop = QDesktopWidget().availableGeometry()
    width = (desktop.width() - window.width()) / 2
    height = (desktop.height() - window.height()) / 2
    window.show()
    window.move(width, height)
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
