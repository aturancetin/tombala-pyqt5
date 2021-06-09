"""
@file: tombala_ui.py

@author: Ali Turan Cetin

@date: June 9, 2021

@brief: Tombala Game with PyQt5
"""

from game import gameFunctions
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """ The function that initalize the user interface."""

        # The Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 599)
        MainWindow.setMinimumSize(QtCore.QSize(801, 599))
        MainWindow.setMaximumSize(QtCore.QSize(801, 599))

        # The Parent Widget of the Application
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # The pop up to show end message
        self.endMessage = QMessageBox(self.centralwidget)
        self.endMessage.setWindowTitle("Game Ended")
        self.endMessage.setStandardButtons(QMessageBox.Cancel)
        self.endMessage.setObjectName("endMessage")

        # The number of left numbers in the bag
        self.bag_count = QLabel(self.centralwidget)
        self.bag_count.setObjectName(u"bag_count")
        self.bag_count.setGeometry(QtCore.QRect(385, 70, 67, 17))

        # The intro cover
        self.cover = QtWidgets.QLabel(self.centralwidget)
        self.cover.setGeometry(QtCore.QRect(0, -20, 801, 581))
        self.cover.setText("")
        self.cover.setPixmap(QtGui.QPixmap("TombalaBG.png"))
        self.cover.setScaledContents(True)
        self.cover.setObjectName("cover")

        # The button to exit the game
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setEnabled(True)
        self.exitButton.setGeometry(QtCore.QRect(440, 480, 201, 51))
        self.exitButton.setStyleSheet(
            "QPushButton {background-color: #E76939; border-radius: 10px; font-size: 30px; } QPushButton:hover{background-color:black; color: white}")
        self.exitButton.setObjectName("exitButton")

        # The button to start the game
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(190, 480, 201, 51))
        self.playButton.setStyleSheet(
            "QPushButton {background-color: #E76939; border-radius: 10px; font-size: 30px; } QPushButton:hover{background-color:black; color: white}")
        self.playButton.setObjectName("playButton")

        # The background image of the game
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PlayGround.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # The card for player 1
        self.card1 = QtWidgets.QLabel(self.centralwidget)
        self.card1.setGeometry(QtCore.QRect(30, 200, 321, 151))
        self.card1.setText("")
        self.card1.setPixmap(QtGui.QPixmap("card.png"))
        self.card1.setScaledContents(True)
        self.card1.setObjectName("card1")

        # The card for player 2
        self.card2 = QtWidgets.QLabel(self.centralwidget)
        self.card2.setGeometry(QtCore.QRect(450, 200, 321, 151))
        self.card2.setText("")
        self.card2.setPixmap(QtGui.QPixmap("card.png"))
        self.card2.setScaledContents(True)
        self.card2.setObjectName("card2")

        # The button to initialize cards and the game
        self.initializeCards = QtWidgets.QPushButton(self.centralwidget)
        self.initializeCards.setGeometry(QtCore.QRect(300, 20, 201, 51))
        self.initializeCards.setStyleSheet(
            "QPushButton {background-color: #E76939; border-radius: 10px; font-size: 20px; } QPushButton:hover{background-color:black; color: white}")
        self.initializeCards.setObjectName("initializeCards")

        # The button to pick a number from the bag
        self.pickANumberButton = QtWidgets.QPushButton(self.centralwidget)
        self.pickANumberButton.setGeometry(QtCore.QRect(300, 20, 201, 51))
        self.pickANumberButton.setStyleSheet(
            "QPushButton {background-color: #E76939; border-radius: 10px; font-size: 20px; } QPushButton:hover{background-color:black; color: white}")
        self.pickANumberButton.setObjectName("pickANumber")

        # The button to restart the game
        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setGeometry(QtCore.QRect(300, 20, 201, 51))
        self.restartButton.setStyleSheet(
            "QPushButton {background-color: #E76939; border-radius: 10px; font-size: 20px; } QPushButton:hover{background-color:black; color: white}")
        self.restartButton.setObjectName("restartButton")

        # The name of player 1
        self.player1 = QtWidgets.QLabel(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(240, 470, 71, 31))
        self.player1.setObjectName("player1")

        # The name of player 2
        self.player2 = QtWidgets.QLabel(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(490, 470, 71, 31))
        self.player2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.player2.setObjectName("player2")

        # PLAYER 1'S CARD - ROW 1

        # player1-row1-stamp1
        self.p1_r1_s1 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r1_s1.setGeometry(QtCore.QRect(73, 216, 31, 31))
        self.p1_r1_s1.setObjectName("p1_r1_s1")
        self.p1_r1_s1.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row1-stamp2
        self.p1_r1_s2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r1_s2.setGeometry(QtCore.QRect(142, 210, 31, 41))
        self.p1_r1_s2.setObjectName("p1_r1_s2")
        self.p1_r1_s2.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row1-stamp3
        self.p1_r1_s3 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r1_s3.setGeometry(QtCore.QRect(211, 210, 31, 41))
        self.p1_r1_s3.setObjectName("p1_r1_s3")
        self.p1_r1_s3.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row1-stamp4
        self.p1_r1_s4 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r1_s4.setGeometry(QtCore.QRect(280, 210, 31, 41))
        self.p1_r1_s4.setObjectName("p1_r1_s4")
        self.p1_r1_s4.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row1-stamp5
        self.p1_r1_s5 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r1_s5.setGeometry(QtCore.QRect(312, 210, 31, 41))
        self.p1_r1_s5.setObjectName("p1_r1_s5")
        self.p1_r1_s5.setStyleSheet(
            "QLabel { font-size: 20px }")

        # PLAYER 1'S CARD - ROW 2

        # player1-row2-stamp5
        self.p1_r2_s5 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r2_s5.setGeometry(QtCore.QRect(312, 260, 31, 41))
        self.p1_r2_s5.setObjectName("p1_r2_s5")
        self.p1_r2_s5.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row2-stamp4
        self.p1_r2_s4 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r2_s4.setGeometry(QtCore.QRect(243, 260, 31, 31))
        self.p1_r2_s4.setObjectName("p1_r2_s4")
        self.p1_r2_s4.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row2-stamp3
        self.p1_r2_s3 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r2_s3.setGeometry(QtCore.QRect(173, 260, 31, 31))
        self.p1_r2_s3.setObjectName("p1_r2_s3")
        self.p1_r2_s3.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row2-stamp2
        self.p1_r2_s2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r2_s2.setGeometry(QtCore.QRect(110, 260, 31, 31))
        self.p1_r2_s2.setObjectName("p1_r2_s2")
        self.p1_r2_s2.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row2-stamp1
        self.p1_r2_s1 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r2_s1.setGeometry(QtCore.QRect(40, 260, 31, 31))
        self.p1_r2_s1.setObjectName("p1_r2_s1")
        self.p1_r2_s1.setStyleSheet(
            "QLabel { font-size: 20px }")

        # PLAYER 1'S CARD - ROW 3

        # player1-row3-stamp1
        self.p1_r3_s1 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r3_s1.setGeometry(QtCore.QRect(70, 300, 31, 41))
        self.p1_r3_s1.setObjectName("p1_r3_s1")
        self.p1_r3_s1.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row3-stamp2
        self.p1_r3_s2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r3_s2.setGeometry(QtCore.QRect(140, 300, 31, 41))
        self.p1_r3_s2.setObjectName("p1_r3_s2")
        self.p1_r3_s2.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row3-stamp3
        self.p1_r3_s3 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r3_s3.setGeometry(QtCore.QRect(210, 300, 31, 41))
        self.p1_r3_s3.setObjectName("p1_r3_s3")
        self.p1_r3_s3.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row3-stamp4
        self.p1_r3_s4 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r3_s4.setGeometry(QtCore.QRect(280, 300, 31, 41))
        self.p1_r3_s4.setObjectName("p1_r3_s4")
        self.p1_r3_s4.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player1-row3-stamp5
        self.p1_r3_s5 = QtWidgets.QLabel(self.centralwidget)
        self.p1_r3_s5.setGeometry(QtCore.QRect(311, 300, 31, 41))
        self.p1_r3_s5.setObjectName("p1_r3_s5")
        self.p1_r3_s5.setStyleSheet(
            "QLabel { font-size: 20px }")

        # PLAYER 2'S CARD - ROW 1

        # player2-row1-stamp1
        self.p2_r1_s1 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r1_s1.setGeometry(QtCore.QRect(492, 216, 31, 31))
        self.p2_r1_s1.setObjectName("p2_r1_s1")
        self.p2_r1_s1.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row1-stamp2
        self.p2_r1_s2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r1_s2.setGeometry(QtCore.QRect(561, 210, 31, 41))
        self.p2_r1_s2.setObjectName("p2_r1_s2")
        self.p2_r1_s2.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row1-stamp3
        self.p2_r1_s3 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r1_s3.setGeometry(QtCore.QRect(630, 210, 31, 41))
        self.p2_r1_s3.setObjectName("p2_r1_s3")
        self.p2_r1_s3.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row1-stamp4
        self.p2_r1_s4 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r1_s4.setGeometry(QtCore.QRect(700, 210, 31, 41))
        self.p2_r1_s4.setObjectName("p2_r1_s4")
        self.p2_r1_s4.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row1-stamp5
        self.p2_r1_s5 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r1_s5.setGeometry(QtCore.QRect(730, 210, 31, 41))
        self.p2_r1_s5.setObjectName("p2_r1_s5")
        self.p2_r1_s5.setStyleSheet(
            "QLabel { font-size: 20px }")

        # PLAYER 2'S CARD - ROW 2

        # player2-row2-stamp1
        self.p2_r2_s1 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r2_s1.setGeometry(QtCore.QRect(460, 260, 31, 31))
        self.p2_r2_s1.setObjectName("p2_r2_s1")
        self.p2_r2_s1.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row2-stamp2
        self.p2_r2_s2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r2_s2.setGeometry(QtCore.QRect(530, 260, 31, 31))
        self.p2_r2_s2.setObjectName("p2_r2_s2")
        self.p2_r2_s2.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row2-stamp3
        self.p2_r2_s3 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r2_s3.setGeometry(QtCore.QRect(593, 260, 31, 31))
        self.p2_r2_s3.setObjectName("p2_r2_s3")
        self.p2_r2_s3.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row2-stamp4
        self.p2_r2_s4 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r2_s4.setGeometry(QtCore.QRect(663, 260, 31, 31))
        self.p2_r2_s4.setObjectName("p2_r2_s4")
        self.p2_r2_s4.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row2-stamp5
        self.p2_r2_s5 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r2_s5.setGeometry(QtCore.QRect(732, 260, 31, 41))
        self.p2_r2_s5.setObjectName("p2_r2_s5")
        self.p2_r2_s5.setStyleSheet(
            "QLabel { font-size: 20px }")

        # PLAYER 2'S CARD - ROW 3

        # player2-row3-stamp1
        self.p2_r3_s1 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r3_s1.setGeometry(QtCore.QRect(490, 300, 31, 41))
        self.p2_r3_s1.setObjectName("p2_r3_s1")
        self.p2_r3_s1.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row3-stamp2
        self.p2_r3_s2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r3_s2.setGeometry(QtCore.QRect(560, 300, 31, 41))
        self.p2_r3_s2.setObjectName("p2_r3_s2")
        self.p2_r3_s2.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row3-stamp3
        self.p2_r3_s3 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r3_s3.setGeometry(QtCore.QRect(630, 300, 31, 41))
        self.p2_r3_s3.setObjectName("p2_r3_s3")
        self.p2_r3_s3.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row3-stamp4
        self.p2_r3_s4 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r3_s4.setGeometry(QtCore.QRect(700, 300, 31, 41))
        self.p2_r3_s4.setObjectName("p2_r3_s4")
        self.p2_r3_s4.setStyleSheet(
            "QLabel { font-size: 20px }")

        # player2-row3-stamp5
        self.p2_r3_s5 = QtWidgets.QLabel(self.centralwidget)
        self.p2_r3_s5.setGeometry(QtCore.QRect(730, 300, 31, 41))
        self.p2_r3_s5.setObjectName("p2_r3_s5")
        self.p2_r3_s5.setStyleSheet(
            "QLabel { font-size: 20px }")

        # The picked number from the bag
        self.pickedNumber = QtWidgets.QLabel(self.centralwidget)
        self.pickedNumber.setGeometry(QtCore.QRect(370, 100, 131, 41))
        self.pickedNumber.setObjectName("pickedNumber")
        self.pickedNumber.setStyleSheet(
            "QLabel { font-size: 50px }")

        # The score of player 1
        self.player1_score = QtWidgets.QLabel(self.centralwidget)
        self.player1_score.setGeometry(QtCore.QRect(90, 460, 71, 41))
        self.player1_score.setObjectName("player1_score")
        self.player1_score.setStyleSheet(
            "QLabel { font-size: 40px }")

        # The score of player 2
        self.player2_score = QtWidgets.QLabel(self.centralwidget)
        self.player2_score.setGeometry(QtCore.QRect(675, 460, 71, 41))
        self.player2_score.setObjectName("player2_score")
        self.player2_score.setStyleSheet(
            "QLabel { font-size: 40px }")

        # Initialization of the number bag
        self.bag = list(range(1, 91))

        # Initialization of the score of player 1
        self.score_of_player1 = 0

        # Initialization of the score of player 1
        self.score_of_player2 = 0

        # Initialization of the card1 array
        self.card1_array = [[self.p1_r1_s1, self.p1_r1_s2, self.p1_r1_s3, self.p1_r1_s4, self.p1_r1_s5], [self.p1_r2_s1, self.p1_r2_s2,
                                                                                                          self.p1_r2_s3, self.p1_r2_s4, self.p1_r2_s5], [self.p1_r3_s1, self.p1_r3_s2, self.p1_r3_s3, self.p1_r3_s4, self.p1_r3_s5]]
        # Initialization of the card1 array
        self.card2_array = [[self.p2_r1_s1, self.p2_r1_s2, self.p2_r1_s3, self.p2_r1_s4, self.p2_r1_s5], [self.p2_r2_s1, self.p2_r2_s2,
                                                                                                          self.p2_r2_s3, self.p2_r2_s4, self.p2_r2_s5], [self.p2_r3_s1, self.p2_r3_s2, self.p2_r3_s3, self.p2_r3_s4, self.p2_r3_s5]]

        # Initialization for copy array 1
        self.card1_copy = np.zeros([3, 5], dtype=np.uint)

        # Initialization for copy array 1
        self.card2_copy = np.zeros([3, 5], dtype=np.uint)

        # Stamp - player1 - row1 - stamp1
        self.stamp_p1_r1_s1 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r1_s1.setObjectName(u"stamp")
        self.stamp_p1_r1_s1.setGeometry(QtCore.QRect(70, 210, 41, 41))
        self.stamp_p1_r1_s1.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r1_s1.setScaledContents(True)

        # Stamp - player1 - row1 - stamp2
        self.stamp_p1_r1_s2 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r1_s2.setObjectName(u"stamp")
        self.stamp_p1_r1_s2.setGeometry(QtCore.QRect(140, 210, 31, 41))
        self.stamp_p1_r1_s2.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r1_s2.setScaledContents(True)

        # Stamp - player1 - row1 - stamp3
        self.stamp_p1_r1_s3 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r1_s3.setObjectName(u"stamp")
        self.stamp_p1_r1_s3.setGeometry(QtCore.QRect(210, 210, 31, 41))
        self.stamp_p1_r1_s3.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r1_s3.setScaledContents(True)

        # Stamp - player1 - row1 - stamp4
        self.stamp_p1_r1_s4 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r1_s4.setObjectName(u"stamp")
        self.stamp_p1_r1_s4.setGeometry(QtCore.QRect(280, 210, 31, 41))
        self.stamp_p1_r1_s4.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r1_s4.setScaledContents(True)

        # Stamp - player1 - row1 - stamp5
        self.stamp_p1_r1_s5 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r1_s5.setObjectName(u"stamp")
        self.stamp_p1_r1_s5.setGeometry(QtCore.QRect(310, 210, 31, 41))
        self.stamp_p1_r1_s5.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r1_s5.setScaledContents(True)

        # Stamp - player1 - row2 - stamp1
        self.stamp_p1_r2_s1 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r2_s1.setObjectName(u"stamp")
        self.stamp_p1_r2_s1.setGeometry(QtCore.QRect(40, 260, 41, 41))
        self.stamp_p1_r2_s1.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r2_s1.setScaledContents(True)

        # Stamp - player1 - row2 - stamp2
        self.stamp_p1_r2_s2 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r2_s2.setObjectName(u"stamp")
        self.stamp_p1_r2_s2.setGeometry(QtCore.QRect(110, 260, 31, 41))
        self.stamp_p1_r2_s2.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r2_s2.setScaledContents(True)

        # Stamp - player1 - row2 - stamp3
        self.stamp_p1_r2_s3 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r2_s3.setObjectName(u"stamp")
        self.stamp_p1_r2_s3.setGeometry(QtCore.QRect(170, 260, 31, 41))
        self.stamp_p1_r2_s3.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r2_s3.setScaledContents(True)

        # Stamp - player1 - row2 - stamp4
        self.stamp_p1_r2_s4 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r2_s4.setObjectName(u"stamp")
        self.stamp_p1_r2_s4.setGeometry(QtCore.QRect(240, 260, 31, 41))
        self.stamp_p1_r2_s4.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r2_s4.setScaledContents(True)

        # Stamp - player1 - row2 - stamp5
        self.stamp_p1_r2_s5 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r2_s5.setObjectName(u"stamp")
        self.stamp_p1_r2_s5.setGeometry(QtCore.QRect(310, 260, 31, 41))
        self.stamp_p1_r2_s5.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r2_s5.setScaledContents(True)

        # Stamp - player1 - row3 - stamp1
        self.stamp_p1_r3_s1 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r3_s1.setObjectName(u"stamp")
        self.stamp_p1_r3_s1.setGeometry(QtCore.QRect(70, 300, 41, 41))
        self.stamp_p1_r3_s1.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r3_s1.setScaledContents(True)

        # Stamp - player1 - row3 - stamp2
        self.stamp_p1_r3_s2 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r3_s2.setObjectName(u"stamp")
        self.stamp_p1_r3_s2.setGeometry(QtCore.QRect(140, 300, 31, 41))
        self.stamp_p1_r3_s2.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r3_s2.setScaledContents(True)

        # Stamp - player1 - row3 - stamp3
        self.stamp_p1_r3_s3 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r3_s3.setObjectName(u"stamp")
        self.stamp_p1_r3_s3.setGeometry(QtCore.QRect(210, 300, 31, 41))
        self.stamp_p1_r3_s3.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r3_s3.setScaledContents(True)

        # Stamp - player1 - row3 - stamp4
        self.stamp_p1_r3_s4 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r3_s4.setObjectName(u"stamp")
        self.stamp_p1_r3_s4.setGeometry(QtCore.QRect(280, 300, 31, 41))
        self.stamp_p1_r3_s4.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r3_s4.setScaledContents(True)

        # Stamp - player1 - row3 - stamp5
        self.stamp_p1_r3_s5 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p1_r3_s5.setObjectName(u"stamp")
        self.stamp_p1_r3_s5.setGeometry(QtCore.QRect(310, 300, 31, 41))
        self.stamp_p1_r3_s5.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p1_r3_s5.setScaledContents(True)

        # Stamp - player2 - row1 - stamp1
        self.stamp_p2_r1_s1 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r1_s1.setObjectName(u"stamp")
        self.stamp_p2_r1_s1.setGeometry(QtCore.QRect(490, 216, 41, 41))
        self.stamp_p2_r1_s1.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r1_s1.setScaledContents(True)

        # Stamp - player2 - row1 - stamp2
        self.stamp_p2_r1_s2 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r1_s2.setObjectName(u"stamp")
        self.stamp_p2_r1_s2.setGeometry(QtCore.QRect(560, 210, 31, 41))
        self.stamp_p2_r1_s2.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r1_s2.setScaledContents(True)

        # Stamp - player2 - row1 - stamp3
        self.stamp_p2_r1_s3 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r1_s3.setObjectName(u"stamp")
        self.stamp_p2_r1_s3.setGeometry(QtCore.QRect(630, 210, 31, 41))
        self.stamp_p2_r1_s3.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r1_s3.setScaledContents(True)

        # Stamp - player2 - row1 - stamp4
        self.stamp_p2_r1_s4 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r1_s4.setObjectName(u"stamp")
        self.stamp_p2_r1_s4.setGeometry(QtCore.QRect(700, 210, 31, 41))
        self.stamp_p2_r1_s4.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r1_s4.setScaledContents(True)

        # Stamp - player2 - row1 - stamp5
        self.stamp_p2_r1_s5 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r1_s5.setObjectName(u"stamp")
        self.stamp_p2_r1_s5.setGeometry(QtCore.QRect(730, 210, 31, 41))
        self.stamp_p2_r1_s5.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r1_s5.setScaledContents(True)

        # Stamp - player2 - row2 - stamp1
        self.stamp_p2_r2_s1 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r2_s1.setObjectName(u"stamp")
        self.stamp_p2_r2_s1.setGeometry(QtCore.QRect(460, 260, 41, 41))
        self.stamp_p2_r2_s1.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r2_s1.setScaledContents(True)

        # Stamp - player2 - row2 - stamp2
        self.stamp_p2_r2_s2 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r2_s2.setObjectName(u"stamp")
        self.stamp_p2_r2_s2.setGeometry(QtCore.QRect(530, 260, 31, 41))
        self.stamp_p2_r2_s2.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r2_s2.setScaledContents(True)

        # Stamp - player2 - row2 - stamp3
        self.stamp_p2_r2_s3 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r2_s3.setObjectName(u"stamp")
        self.stamp_p2_r2_s3.setGeometry(QtCore.QRect(590, 260, 31, 41))
        self.stamp_p2_r2_s3.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r2_s3.setScaledContents(True)

        # Stamp - player2 - row2 - stamp4
        self.stamp_p2_r2_s4 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r2_s4.setObjectName(u"stamp")
        self.stamp_p2_r2_s4.setGeometry(QtCore.QRect(660, 260, 31, 41))
        self.stamp_p2_r2_s4.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r2_s4.setScaledContents(True)

        # Stamp - player2 - row2 - stamp5
        self.stamp_p2_r2_s5 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r2_s5.setObjectName(u"stamp")
        self.stamp_p2_r2_s5.setGeometry(QtCore.QRect(730, 260, 31, 41))
        self.stamp_p2_r2_s5.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r2_s5.setScaledContents(True)

        # Stamp - player2 - row3 - stamp1
        self.stamp_p2_r3_s1 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r3_s1.setObjectName(u"stamp")
        self.stamp_p2_r3_s1.setGeometry(QtCore.QRect(490, 300, 41, 41))
        self.stamp_p2_r3_s1.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r3_s1.setScaledContents(True)

        # Stamp - player2 - row3 - stamp2
        self.stamp_p2_r3_s2 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r3_s2.setObjectName(u"stamp")
        self.stamp_p2_r3_s2.setGeometry(QtCore.QRect(560, 300, 31, 41))
        self.stamp_p2_r3_s2.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r3_s2.setScaledContents(True)

        # Stamp - player2 - row3 - stamp3
        self.stamp_p2_r3_s3 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r3_s3.setObjectName(u"stamp")
        self.stamp_p2_r3_s3.setGeometry(QtCore.QRect(630, 300, 31, 41))
        self.stamp_p2_r3_s3.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r3_s3.setScaledContents(True)

        # Stamp - player2 - row3 - stamp4
        self.stamp_p2_r3_s4 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r3_s4.setObjectName(u"stamp")
        self.stamp_p2_r3_s4.setGeometry(QtCore.QRect(700, 300, 31, 41))
        self.stamp_p2_r3_s4.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r3_s4.setScaledContents(True)

        # Stamp - player2 - row3 - stamp5
        self.stamp_p2_r3_s5 = QtWidgets.QLabel(self.centralwidget)
        self.stamp_p2_r3_s5.setObjectName(u"stamp")
        self.stamp_p2_r3_s5.setGeometry(QtCore.QRect(730, 300, 31, 41))
        self.stamp_p2_r3_s5.setPixmap(QtGui.QPixmap(u"stamp.png"))
        self.stamp_p2_r3_s5.setScaledContents(True)

        # Bingo ticks for player 1
        self.p1_bingo1 = QtWidgets.QLabel(self.centralwidget)
        self.p1_bingo1.setObjectName(u"p1_bingo1")
        self.p1_bingo1.setGeometry(QtCore.QRect(160, 40, 31, 31))
        self.p1_bingo1.setPixmap(QtGui.QPixmap(u"tick.png"))
        self.p1_bingo1.setScaledContents(True)
        self.p1_bingo2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_bingo2.setObjectName(u"p1_bingo2")
        self.p1_bingo2.setGeometry(QtCore.QRect(190, 70, 31, 31))
        self.p1_bingo2.setPixmap(QtGui.QPixmap(u"tick.png"))
        self.p1_bingo2.setScaledContents(True)
        self.p1_bingo3 = QtWidgets.QLabel(self.centralwidget)
        self.p1_bingo3.setObjectName(u"p1_bingo3")
        self.p1_bingo3.setGeometry(QtCore.QRect(170, 100, 31, 31))
        self.p1_bingo3.setPixmap(QtGui.QPixmap(u"tick.png"))
        self.p1_bingo3.setScaledContents(True)

        # Bingo ticks for player 2
        self.p2_bingo1 = QtWidgets.QLabel(self.centralwidget)
        self.p2_bingo1.setObjectName(u"p2_bingo1")
        self.p2_bingo1.setGeometry(QtCore.QRect(610, 40, 31, 31))
        self.p2_bingo1.setPixmap(QtGui.QPixmap(u"tick.png"))
        self.p2_bingo1.setScaledContents(True)
        self.p2_bingo3 = QtWidgets.QLabel(self.centralwidget)
        self.p2_bingo3.setObjectName(u"p2_bingo3")
        self.p2_bingo3.setGeometry(QtCore.QRect(600, 100, 31, 31))
        self.p2_bingo3.setPixmap(QtGui.QPixmap(u"tick.png"))
        self.p2_bingo3.setScaledContents(True)
        self.p2_bingo2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_bingo2.setObjectName(u"p2_bingo2")
        self.p2_bingo2.setGeometry(QtCore.QRect(580, 70, 31, 31))
        self.p2_bingo2.setPixmap(QtGui.QPixmap(u"tick.png"))
        self.p2_bingo2.setScaledContents(True)

        # Store stamps of player1 in an array
        self.stamp_array1 = [[self.stamp_p1_r1_s1, self.stamp_p1_r1_s2, self.stamp_p1_r1_s3, self.stamp_p1_r1_s4, self.stamp_p1_r1_s5, ], [self.stamp_p1_r2_s1, self.stamp_p1_r2_s2,
                                                                                                                                           self.stamp_p1_r2_s3, self.stamp_p1_r2_s4, self.stamp_p1_r2_s5, ], [self.stamp_p1_r3_s1, self.stamp_p1_r3_s2, self.stamp_p1_r3_s3, self.stamp_p1_r3_s4, self.stamp_p1_r3_s5, ]]

        # Store stamps of player2 in an array
        self.stamp_array2 = [[self.stamp_p2_r1_s1, self.stamp_p2_r1_s2, self.stamp_p2_r1_s3, self.stamp_p2_r1_s4, self.stamp_p2_r1_s5, ], [self.stamp_p2_r2_s1, self.stamp_p2_r2_s2,
                                                                                                                                           self.stamp_p2_r2_s3, self.stamp_p2_r2_s4, self.stamp_p2_r2_s5, ], [self.stamp_p2_r3_s1, self.stamp_p2_r3_s2, self.stamp_p2_r3_s3, self.stamp_p2_r3_s4, self.stamp_p2_r3_s5, ]]

        # Initialization of the bingo array for player 1
        self.bingoArray1 = [self.p1_bingo1, self.p1_bingo2, self.p1_bingo3]

        # Initialization of the bingo array for player 2
        self.bingoArray2 = [self.p2_bingo1, self.p2_bingo2, self.p2_bingo3]

        # Necessary widgets are brought forward respectively
        self.label.raise_()
        self.card1.raise_()
        self.initializeCards.raise_()
        self.p2_r1_s5.raise_()
        self.p2_r2_s2.raise_()
        self.p1_r3_s4.raise_()
        self.p1_r3_s5.raise_()
        self.p1_r1_s2.raise_()
        self.p2_r2_s4.raise_()
        self.card2.raise_()
        self.p1_r3_s3.raise_()
        self.p1_r1_s4.raise_()
        self.p1_r1_s3.raise_()
        self.player2.raise_()
        self.p2_r2_s5.raise_()
        self.p1_r2_s2.raise_()
        self.p1_r2_s1.raise_()
        self.p1_r2_s3.raise_()
        self.p2_r2_s1.raise_()
        self.p1_r1_s5.raise_()
        self.p2_r3_s4.raise_()
        self.p1_r1_s1.raise_()
        self.p2_r1_s4.raise_()
        self.p1_r3_s1.raise_()
        self.p2_r1_s2.raise_()
        self.p1_r2_s4.raise_()
        self.p2_r1_s1.raise_()
        self.p2_r1_s3.raise_()
        self.p2_r2_s3.raise_()
        self.p2_r3_s2.raise_()
        self.pickANumberButton.raise_()
        self.p2_r3_s3.raise_()
        self.player1.raise_()
        self.p2_r3_s5.raise_()
        self.p2_r3_s1.raise_()
        self.p1_r3_s2.raise_()
        self.p1_r2_s5.raise_()
        self.pickedNumber.raise_()
        self.cover.raise_()
        self.playButton.raise_()
        self.exitButton.raise_()

        # The top menu and actions
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionMenu = QtWidgets.QAction(MainWindow)
        self.actionMenu.setObjectName("actionMenu")
        self.menuMenu.addAction(self.actionMenu)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)

        # Close action is triggered when the exit button is pressed
        self.exitButton.clicked.connect(MainWindow.close)

        # Necessary UI changes are implemented when the play button is pressed
        self.playButton.clicked.connect(self.cover.hide)
        self.playButton.clicked.connect(self.playButton.hide)
        self.playButton.clicked.connect(self.exitButton.hide)
        self.playButton.clicked.connect(self.initializeCards.raise_)

        # Necessary UI changes are implemented when the initialize cards button is pressed
        self.initializeCards.clicked.connect(self.initializeCards.hide)
        self.initializeCards.clicked.connect(self.pickANumberButton.raise_)
        self.initializeCards.clicked.connect(self.card1.raise_)
        self.initializeCards.clicked.connect(self.card2.raise_)
        self.initializeCards.clicked.connect(self.player1_score.raise_)
        self.initializeCards.clicked.connect(self.player2_score.raise_)
        self.initializeCards.clicked.connect(lambda:
                                             gameFunctions.setNumbers(self.card1_array, self.card2_array, self.card1_copy, self.card2_copy))

        # The function responsible for picking a number is called when the pick a number button is pressed
        self.pickANumberButton.clicked.connect(
            lambda: gameFunctions.pickANumber(self.restartButton, self.endMessage, self.player1, self.player2, self.bag_count, self.bag,  self.pickedNumber, self.stamp_array1, self.stamp_array2, self.card1_array, self.card2_array, self.card1_copy, self.card2_copy, self.bingoArray1, self.bingoArray2, self.player1_score, self.player2_score))

        # The game restarts when the restart button is pressed
        self.restartButton.clicked.connect(gameFunctions.restart)

        # The game restarts when the menu button is pressed
        self.actionMenu.triggered.connect(gameFunctions.restart)

        # The game closes when the exit button is pressed
        self.actionExit.triggered.connect(MainWindow.close)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """Function that handles the translation of the string properties of the form"""

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.endMessage.setText(_translate("MainWindow", ""))
        self.playButton.setText(_translate("MainWindow", "PLAY"))
        self.initializeCards.setText(
            _translate("MainWindow", "INITIALIZE CARDS"))
        self.pickANumberButton.setText(
            _translate("MainWindow", "PICK A NUMBER"))
        self.restartButton.setText(
            _translate("MainWindow", "RESTART GAME"))
        self.player1.setText(_translate("MainWindow", "Player 1"))
        self.player2.setText(_translate("MainWindow", "Player 2"))
        self.p1_r1_s1.setText(_translate("MainWindow", ""))
        self.p1_r1_s2.setText(_translate("MainWindow", ""))
        self.p1_r1_s3.setText(_translate("MainWindow", ""))
        self.p1_r1_s4.setText(_translate("MainWindow", ""))
        self.p1_r1_s5.setText(_translate("MainWindow", ""))
        self.p1_r2_s5.setText(_translate("MainWindow", ""))
        self.p1_r2_s4.setText(_translate("MainWindow", ""))
        self.p1_r2_s3.setText(_translate("MainWindow", ""))
        self.p1_r2_s2.setText(_translate("MainWindow", ""))
        self.p1_r2_s1.setText(_translate("MainWindow", ""))
        self.p1_r3_s1.setText(_translate("MainWindow", ""))
        self.p1_r3_s2.setText(_translate("MainWindow", ""))
        self.p1_r3_s3.setText(_translate("MainWindow", ""))
        self.p1_r3_s4.setText(_translate("MainWindow", ""))
        self.p1_r3_s5.setText(_translate("MainWindow", ""))
        self.p2_r1_s5.setText(_translate("MainWindow", ""))
        self.p2_r1_s2.setText(_translate("MainWindow", ""))
        self.p2_r2_s5.setText(_translate("MainWindow", ""))
        self.p2_r3_s1.setText(_translate("MainWindow", ""))
        self.p2_r1_s3.setText(_translate("MainWindow", ""))
        self.p2_r2_s3.setText(_translate("MainWindow", ""))
        self.p2_r3_s4.setText(_translate("MainWindow", ""))
        self.p2_r2_s1.setText(_translate("MainWindow", ""))
        self.p2_r3_s2.setText(_translate("MainWindow", ""))
        self.p2_r1_s4.setText(_translate("MainWindow", ""))
        self.p2_r3_s5.setText(_translate("MainWindow", ""))
        self.p2_r1_s1.setText(_translate("MainWindow", ""))
        self.p2_r2_s4.setText(_translate("MainWindow", ""))
        self.p2_r2_s2.setText(_translate("MainWindow", ""))
        self.p2_r3_s3.setText(_translate("MainWindow", ""))
        self.pickedNumber.setText(_translate("MainWindow", " "))
        self.player1_score.setText(_translate("MainWindow", "0"))
        self.player2_score.setText(_translate("MainWindow", "0"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionMenu.setText(_translate("MainWindow", "Menu"))
