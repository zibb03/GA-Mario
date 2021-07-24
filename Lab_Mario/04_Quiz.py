# 02. pyqt_widget.py
# PyQt 위젯
import retro
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication,\
    QWidget, QLabel, QPushButton
import numpy as np

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 창 크기 고정
        self.setFixedSize(480, 448)
        # 창 제목 설정
        self.setWindowTitle('GA Mario')

        # 이미지
        self.label_image = QLabel(self)

        # 게임 환경 생성
        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 새 게임 시작
        self.env.reset()
        # 화면 가져오기
        self.screen = self.env.get_screen()

        print(self.screen)

        qimage = QImage(self.screen, self.screen.shape[1], self.screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)

        # 타이머 생성
        self.qtimer = QTimer(self)
        # 타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.game_timer)
        # 1초(1000밀리초)마다 연결된 함수를 실행
        self.qtimer.start(10000)

        self.show()

    def update_screen(self):
        # 화면 가져오기
        self.screen = self.env.get_screen()
        screen_qimage = QImage(self.screen, self.screen.shape[1], self.screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(screen_qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)
        #pixmap = pixmap.scaled(self.screen_width, self.screen_height, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)

    def game_timer(self):
        # 키 배열: B, NULL, SELECT, START, U, D, L, R, A
        self.env.step(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.update_screen()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyApp()
   sys.exit(app.exec_())