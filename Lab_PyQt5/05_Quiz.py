# 01. pyqt_timer.py
# PyQt5 타이머 예제

import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # 창 크기 고정
        self.setFixedSize(400, 300)
        # 창 제목 설정
        self.setWindowTitle('GA Mario')

        # 초 변수 생성
        self.num = 0

        self.label = QLabel(self)
        self.label.setGeometry(200, 150, 50, 100)

        # 타이머 생성
        self.qtimer = QTimer(self)
        # 타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.timer)
        # 1초(1000밀리초)마다 연결된 함수를 실행
        self.qtimer.start(1000)


        # 창 띄우기
        self.show()

    def timer(self):
        self.num = self.num + 1
        print(self.num)
        self.label.setText(str(self.num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())