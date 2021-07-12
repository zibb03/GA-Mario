# 03. pyqt_paint_event.py
# PyQt Paint Event
import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 300)
        self.setWindowTitle('GA Mario')
        self.show()

    # QWidget 에서 특정 상황에 자동으로 호출해주는 paintEvent
    # 창이 업데이트 될 때마다 실행되는 함수
    def paintEvent(self, event):
        # 그리기 도구
        painter = QPainter()
        # 그리기 시작
        painter.begin(self)

        # 펜 설정 (테두리)
        # 선 그리기 - 색, 굵기, 선 종류(실선)
        #painter.setPen(QPen(Qt.blue, 2.0, Qt.SolidLine))
        #painter.drawLine(0, 10, 200, 100)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.blue))
        # 직사각형 (왼쪽 위, 오른쪽 아래)
        painter.drawRect(0, 0, 50, 50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.NoBrush))
        # 직사각형 (왼쪽 위, 오른쪽 아래)
        painter.drawRect(0, 50, 50, 50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.NoBrush))
        # 직사각형 (왼쪽 위, 오른쪽 아래)
        painter.drawRect(50, 0, 50, 50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.red))
        # 직사각형 (왼쪽 위, 오른쪽 아래)
        painter.drawRect(50, 50, 50, 50)

        # 펜 설정 (테두리)
        # 선 그리기 - 색, 굵기, 선 종류(실선)
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        painter.drawLine(25, 175, 75, 275)

        # 펜 설정 (테두리)
        # 선 그리기 - 색, 굵기, 선 종류(실선)
        painter.setPen(QPen(Qt.blue, 2.0, Qt.SolidLine))
        painter.drawLine(75, 175, 75, 275)

        # 펜 설정 (테두리)
        # 선 그리기 - 색, 굵기, 선 종류(실선)
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        painter.drawLine(125, 175, 75, 275)

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(Qt.cyan))
        # 타원 그리기 - 왼쪽 위 점, 가로 변 지름, 세로 변 지름
        painter.drawEllipse(0, 150, 50, 50)

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(QColor.fromRgb(255, 255, 255)))
        # 타원 그리기 - 왼쪽 위 점, 가로 변 지름, 세로 변 지름
        painter.drawEllipse(50, 150, 50, 50)

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(Qt.cyan))
        # 타원 그리기 - 왼쪽 위 점, 가로 변 지름, 세로 변 지름
        painter.drawEllipse(100, 150, 50, 50)

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(Qt.gray))
        # 타원 그리기 - 왼쪽 위 점, 가로 변 지름, 세로 변 지름
        painter.drawEllipse(50, 250, 50, 50)

        # cyan - 청록색(?)
        #painter.setPen(QPen(Qt.cyan, 1.0, Qt.SolidLine))
        #브러쉬 초기화
        #painter.setBrush(Qt.NoBrush)
        # 텍스트 그리기
        #painter.drawText(0, 250, 'abcd')

        painter.end()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyApp()
   sys.exit(app.exec_())
