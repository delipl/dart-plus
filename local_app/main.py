import serial
import time
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QInputDialog, QLineEdit
from PyQt5.QtWidgets import QLCDNumber
# from multiprocessing import Process
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QCoreApplication, QThread
from PyQt5 import uic

numberOfPlayers = 0
maxValue = 0
app = QApplication([])
actualPlayerName = QLabel()

font = QFont()
font.setBold(True)
font.setPointSize(200)
actualPlayerName.setFont(font)
LCD = QLCDNumber(5)
button = QPushButton("Next player")
next = False

def nextPlayer():
    global next
    next = True

button.clicked.connect(nextPlayer)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setWindowTitle("Open Dart")
        self.layout.addWidget(QLabel("Witamy w Open Dart"))

        self.layout.addWidget(actualPlayerName)

        numberOfPlayers, okPressed = QInputDialog.getText(self, "Players", "How many players", QLineEdit.Normal, "")
        maxValue, okPressed = QInputDialog.getText(self, "Points", "How many points", QLineEdit.Normal, "")

        self.layout.addWidget(LCD)

        self.layout.addWidget(button)

        # startGame()
        for i in range(int(numberOfPlayers)):
            tempPlayerName, okPressed = QInputDialog.getText(self, "Players", "Player name " + str(i + 1),
                                                             QLineEdit.Normal, "")
            players.append(Player(tempPlayerName, i, maxValue))

        # self.button = QPushButton('Start dart')
        # self.button.clicked.connect(self.game)

        # self.layout.addWidget(self.button)
        self.setLayout(self.layout)


def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result


class Player:
    def __init__(self, name, id, points=301):
        self.name = name
        self.id = id
        self.points = int(points)
        self.saved = 0

    def throwing(self, throw):
        if throw > self.points:
            # self.points = self.points + self.throw
            return -1  # przerzucil za duzo
        elif throw == self.points:
            # self.resetThrowing()
            return 1  # wygrywa
        else:
            self.points = self.points - throw
            return 0  # gra dalej




arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
players = []


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


class Game(QThread):
    def run(self):
        global next


        while True:
            for player in players:
                print("Teraz rzuca ", player.name)
                LCD.display(player.points)
                actualPlayerName.setText(player.name)
                # self.show()
                saved = player.points
                for i in range(3):
                    value = write_read('0')
                    time.sleep(0.1)
                        
                    stat = False

                    while len(value) <= 0:
                        value = write_read('0')
                        time.sleep(0.1)
                        if next == True:
                            stat = True
                            break
                        continue

                    if stat:
                        break


                    value = int(value.decode('UTF-8'))
                    status = player.throwing(value)
                    print("Trafiles ", value)





                    if status == -1:
                        print("Gracz ", player.name, " przerzucil !")
                        for j in range(3):
                            player.points = saved
                        break
                    elif status == 1:
                        print("Gracz ", player.name, " wygral !")
                        players.remove(player)
                        if (len(players) == 1):
                            exit(0)
                    elif status == 0:
                        print("Rzut ", i + 1, " Zostalo: ", player.points, " punktow")
                    LCD.display(player.points)
                    # time.sleep(1000)

                next = False
                print(player.name, " zostalo ", player.points, " do konca")

    # startGame()
    # for i in players:
    #     print("Gracz", i.name, " punkty: ", i.points)


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = MainWindow()
    # ex.show()
    # sys.exit(app.exec_())

    ex = MainWindow()
    ex.show()
    thread = Game()
    thread.finished.connect(app.exit)
    thread.start()
    sys.exit(app.exec_())

    # # process1.join()
    # process2.join()

