# 04. pyqt_key_event.py
# PyQt 키 이벤트
import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 창 크기 고정
        self.setFixedSize(400, 300)
        # 창 제목 설정
        self.setWindowTitle('MyApp')

        self.label = QLabel(self)
        self.label.setGeometry(200, 150, 50, 100)

        # 창 띄우기
        self.show()

    def paintEvent(self, event):
        # 그리기 도구
        self.painter = QPainter(self)
        # 그리기 시작
        self.painter.begin(self)

        # 펜 설정 (테두리)
        # 선 그리기 - 색, 굵기, 선 종류(실선)
        # painter.setPen(QPen(Qt.blue, 2.0, Qt.SolidLine))
        # painter.drawLine(0, 10, 200, 100)

        # RGB 색상으로 펜 설정
        self.painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        self.painter.setBrush(QBrush(Qt.blue))
        # 직사각형 (왼쪽 위, 오른쪽 아래)
        self.painter.drawRect(0, 0, 50, 50)

        # RGB 색상으로 펜 설정
        self.painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        self.painter.setBrush(QBrush(Qt.NoBrush))
        # 직사각형 (왼쪽 위, 오른쪽 아래)
        self.painter.drawRect(0, 50, 50, 50)

        # RGB 색상으로 펜 설정
        self.painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        self.painter.setBrush(QBrush(Qt.NoBrush))
        # 직사각형 (왼쪽 위, 오른쪽 아래)
        self.painter.drawRect(50, 0, 50, 50)

        # RGB 색상으로 펜 설정
        self.painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        self.painter.setBrush(QBrush(Qt.red))
        # 직사각형 (왼쪽 위, 오른쪽 아래)
        self.painter.drawRect(50, 50, 50, 50)

        # 펜 설정 (테두리)
        # 선 그리기 - 색, 굵기, 선 종류(실선)
        self.painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        self.painter.drawLine(25, 175, 75, 275)

        # 펜 설정 (테두리)
        # 선 그리기 - 색, 굵기, 선 종류(실선)
        self.painter.setPen(QPen(Qt.blue, 2.0, Qt.SolidLine))
        self.painter.drawLine(75, 175, 75, 275)

        # 펜 설정 (테두리)
        # 선 그리기 - 색, 굵기, 선 종류(실선)
        self.painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        self.painter.drawLine(125, 175, 75, 275)

        self.painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        self.painter.setBrush(QBrush(Qt.cyan))
        # 타원 그리기 - 왼쪽 위 점, 가로 변 지름, 세로 변 지름
        self.painter.drawEllipse(0, 150, 50, 50)

        self.painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        self.painter.setBrush(QBrush(QColor.fromRgb(255, 255, 255)))
        # 타원 그리기 - 왼쪽 위 점, 가로 변 지름, 세로 변 지름
        self.painter.drawEllipse(50, 150, 50, 50)

        self.painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        self.painter.setBrush(QBrush(Qt.cyan))
        # 타원 그리기 - 왼쪽 위 점, 가로 변 지름, 세로 변 지름
        self.painter.drawEllipse(100, 150, 50, 50)

        self.painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        self.painter.setBrush(QBrush(Qt.gray))
        # 타원 그리기 - 왼쪽 위 점, 가로 변 지름, 세로 변 지름
        self.painter.drawEllipse(50, 250, 50, 50)

        # cyan - 청록색(?)
        # painter.setPen(QPen(Qt.cyan, 1.0, Qt.SolidLine))
        # 브러쉬 초기화
        # painter.setBrush(Qt.NoBrush)
        # 텍스트 그리기
        # painter.drawText(0, 250, 'abcd')

        self.painter.end()

    # 키를 누를 때
    def keyPressEvent(self, event):
        self.painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        self.painter.setBrush(QBrush(Qt.gray))
        # 타원 그리기 - 왼쪽 위 점, 가로 변 지름, 세로 변 지름
        self.painter.drawEllipse(50, 300, 50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())