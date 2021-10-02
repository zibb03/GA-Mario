# 02. pyqt_widget.py
# PyQt 위젯
import retro
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
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
        label_image = QLabel(self)

        #image = np.array([[[255, 255, 255], [255, 255, 255]], [[255, 255, 255], [255, 255, 255]]])
        # 게임 환경 생성
        env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 새 게임 시작
        env.reset()
        # 화면 가져오기
        screen = env.get_screen()

        print(screen)

        qimage = QImage(screen, screen.shape[1], screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)

        label_image.setPixmap(pixmap)
        #label_image.setGeometry(0, 0, 100, 100)

        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyApp()
   sys.exit(app.exec_())