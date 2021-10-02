# [도전과제14]
# 05. fitness.py 에 적합도 기준을 참고해서 나만의 적합도 식 만들어보기 (def fitness 함수 만들기)

import retro
import sys
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication,\
    QWidget, QLabel, QPushButton
import tensorflow as tf
import numpy as np

relu = lambda x: np.maximum(0, x)
sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))

class Chromosome:
    def __init__(self):
        self.w1 = np.random.uniform(low=-1, high=1, size=(13 * 16, 9))
        self.b1 = np.random.uniform(low=-1, high=1, size=(9,))

        self.w2 = np.random.uniform(low=-1, high=1, size=(9, 6))
        self.b2 = np.random.uniform(low=-1, high=1, size=(6,))

        self.distance = 0
        self.max_distance = 0
        self.frames = 0
        self.stop_frames = 0
        self.win = 0

    def predict(self, data):
        l1 = relu(np.matmul(data, self.w1) + self.b1)
        output = sigmoid(np.matmul(l1, self.w2) + self.b2)
        result = (output > 0.5).astype(np.int)
        return result

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 창 크기 고정
        self.setFixedSize(820, 448)
        # 창 제목 설정
        self.setWindowTitle('GA Mario')
        self.press_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # 이미지
        self.label_image = QLabel(self)

        # 게임 환경 생성
        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 새 게임 시작
        self.env.reset()
        # 화면 가져오기
        self.screen = self.env.get_screen()
        self.ram = self.env.get_ram()

        qimage = QImage(self.screen, self.screen.shape[1], self.screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)

        self.frame = 0

        # 타이머 생성
        self.qtimer = QTimer(self)
        # 타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.game_timer)
        # 1초(1000밀리초)마다 연결된 함수를 실행
        self.qtimer.start(1000 / 60)

        self.show()

    def paintEvent(self, event):
        self.ram = self.env.get_ram()

        # 위쪽 타일 배열
        full_screen_tiles = self.ram[0x0500:0x069F + 1]
        full_screen_tile_count = full_screen_tiles.shape[0]

        # 정수여야 해서 / 2개
        full_screen_page1_tile = full_screen_tiles[0:full_screen_tile_count // 2].reshape((13, 16))
        full_screen_page2_tile = full_screen_tiles[full_screen_tile_count // 2:].reshape((13, 16))

        full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)

        # 아래쪽 타일 배열
        # 0x071A	Current screen (in level)
        # 현재 화면이 속한 페이지 번호
        current_screen_page = self.ram[0x071A]
        # 0x071C	ScreenEdge X-Position, loads next screen when player past it?
        # 페이지 속 현재 화면 위치
        screen_position = self.ram[0x071C]
        # 화면 오프셋
        screen_offset = (256 * current_screen_page + screen_position) % 512
        # 타일 화면 오프셋
        screen_tile_offset = screen_offset // 16

        # 그리기 도구
        painter = QPainter()
        # 그리기 시작
        painter.begin(self)

        # 481부터 그리기
        # Gray 107 107 107
        # RGB 색상으로 펜 설정
        c = full_screen_tiles.shape[0]

        cnt = 0
        a = 0
        b = 0
        t = 0

        enemy_drawn = self.ram[0x000F:0x0013 + 1]

        for i in range(5):
            # print(enemy_drawn[i])
            if enemy_drawn[i] == 1:
                enemy_horizon_position = self.ram[0x006E:0x0072 + 1]
                # 0x0087-0x008B	Enemy x position on screen
                # 자신이 속한 페이지 속 x 좌표
                enemy_screen_position_x = self.ram[0x0087:0x008B + 1]
                # 0x00CF-0x00D3	Enemy y pos on screen
                enemy_position_y = self.ram[0x00CF:0x00D3 + 1]
                # 적 x 좌표
                enemy_position_x = (enemy_horizon_position * 256 + enemy_screen_position_x) % 512

                # print(enemy_position_x, enemy_position_y)

                # 적 타일 좌표
                enemy_tile_position_x = (enemy_position_x + 8) // 16
                enemy_tile_position_y = (enemy_position_y - 8) // 16 - 1

                # print(enemy_tile_position_x, enemy_tile_position_y)

                # painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
                # 브러쉬 설정 (채우기)
                # painter.setBrush(QBrush(Qt.red))
                # print(1)
                # painter.drawRect(480 + enemy_tile_position_x[i] * 10, enemy_tile_position_y[i] * 10, 10, 10)
                # print(2)
                print(enemy_tile_position_x[i], enemy_tile_position_y[i])
                x = enemy_tile_position_x[i]
                y = enemy_tile_position_y[i]
                if y >= 0 and y < 13 and x >= 0 and x < 32:
                    full_screen_tiles[y][x] = 2

        t = 0

        # 위 타일
        for i in range(416):
            cnt += 1
            if full_screen_tiles[t][i % 32] == 2:
                # print(t, i % 16)
                painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
                # 브러쉬 설정 (채우기)
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(480 + a, 0 + b, 10, 10)
            elif full_screen_tiles[t][i % 32] == 0:
                painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
                # 브러쉬 설정 (채우기)
                painter.setBrush(QBrush(Qt.gray))
                painter.drawRect(480 + a, 0 + b, 10, 10)
            else:
                painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
                # 브러쉬 설정 (채우기)
                painter.setBrush(QBrush(Qt.cyan))
                painter.drawRect(480 + a, 0 + b, 10, 10)
            a += 10
            if cnt % 32 == 0:
                a = 0
                b += 10
                t += 1
        t = 0

        # 현재 화면 추출
        screen_tiles = np.concatenate((full_screen_tiles, full_screen_tiles), axis=1)[:,
                       screen_tile_offset:screen_tile_offset + 16]

        for i in range(208):
            cnt += 1
            if screen_tiles[t][i % 16] == 2:
                painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
                # 브러쉬 설정 (채우기)
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(480 + a, 20 + b, 10, 10)
            elif screen_tiles[t][i % 16] == 0:
                painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
                # 브러쉬 설정 (채우기)
                painter.setBrush(QBrush(Qt.gray))
                painter.drawRect(480 + a, 20 + b, 10, 10)
            else:
                painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
                # 브러쉬 설정 (채우기)
                painter.setBrush(QBrush(Qt.cyan))
                painter.drawRect(480 + a, 20 + b, 10, 10)
            a += 10
            # print(cnt)
            if cnt % 16 == 0:
                a = 0
                b += 10
                t += 1

        # 0x03AD	Player x pos within current screen offset
        # 현재 화면 속 플레이어 x 좌표
        player_position_x = self.ram[0x03AD]
        # 0x03B8	Player y pos within current screen
        # 현재 화면 속 플레이어 y 좌표
        player_position_y = self.ram[0x03B8]

        # 타일 좌표로 변환
        player_tile_position_x = (player_position_x + 8) // 16
        player_tile_position_y = (player_position_y + 8) // 16 - 1

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.blue))
        painter.drawRect(480 + player_tile_position_x * 10, 150 + player_tile_position_y * 10, 10, 10)

        result = Chromosome()
        screen_tiles_2 = screen_tiles.reshape((13 * 16, ))
        a = result.predict(screen_tiles_2)

        self.press_buttons[0] = a[0]
        self.press_buttons[4] = a[1]
        self.press_buttons[5] = a[2]
        self.press_buttons[6] = a[3]
        self.press_buttons[7] = a[4]
        self.press_buttons[8] = a[5]

        win = 0
        fitness = 0
        before = 0
        player_horizon_position = self.ram[0x006D]
        # 0x0086	Player x position on screen
        # 페이지 속 플레이어 x 좌표
        player_screen_position_x = self.ram[0x0086]
        distance = 256 * player_horizon_position + player_screen_position_x
        # print(distance)

        player_float_state = self.ram[0x001D]
        if player_float_state == 0x03:
            win = 1
            # 1.
            fitness += distance * 2
            # 2.
            fitness += distance - self.frame
            # 3.
            fitness += win * 1000000
            print(fitness)
            print('클리어')

        # 0x000E	Player's state
        # 0x06, 0x0B - 게임 오버
        player_state = self.ram[0x000E]
        if player_state == 0x06 or player_state == 0x0B:
            print('게임 오버 1')
            # 1.
            fitness += distance * 2
            # 2.
            fitness += distance - self.frame
            # 3.
            fitness += win * 1000000
            print(fitness)

        # 0x00B5	Player vertical screen position
        # anywhere below viewport is >1
        player_vertical_screen_position = self.ram[0x00B5]
        if player_vertical_screen_position >= 2:
            print('게임 오버 2')
            # 1.
            fitness += distance * 2
            # 2.
            fitness += distance - self.frame
            # 3.
            fitness += win * 1000000
            print(fitness)

    def update_screen(self):
        # 화면 가져오기
        self.screen = self.env.get_screen()

        screen_qimage = QImage(self.screen, self.screen.shape[1], self.screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(screen_qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)

    def game_timer(self):
        self.frame += 1
        self.env.step(self.press_buttons)
        self.update_screen()
        self.update()

    def keyPressEvent(self, event):
        key = event.key()
        if key == 16777235:
            self.press_buttons[4] = 1
        elif key == 16777237:
            self.press_buttons[5] = 1
        elif key == 16777234:
            self.press_buttons[6] = 1
        elif key == 16777236:
            self.press_buttons[7] = 1
        elif key == 65:
            self.press_buttons[8] = 1
        elif key == 66:
            self.press_buttons[0] = 1

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == 16777235:
            self.press_buttons[4] = 0
        elif key == 16777237:
            self.press_buttons[5] = 0
        elif key == 16777234:
            self.press_buttons[6] = 0
        elif key == 16777236:
            self.press_buttons[7] = 0
        elif key == 65:
            self.press_buttons[8] = 0
        elif key == 66:
            self.press_buttons[0] = 0

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyApp()
   sys.exit(app.exec_())