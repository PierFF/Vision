import sys
from PyQt5.QtWidgets import QApplication
from test_bench import TestBench


def run():
    app = QApplication(sys.argv)
    window = TestBench()
    window.showMaximized()
    sys.exit(app.exec_())
