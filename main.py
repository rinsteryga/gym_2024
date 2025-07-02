import sys
from PyQt5.QtWidgets import QApplication
from Main_module import Main

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec_())
