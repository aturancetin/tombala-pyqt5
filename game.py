"""
@file: game.py

@author: Ali Turan Cetin

@date: June 9, 2021

@brief: Tombala Game with PyQt5
"""

import numpy as np
import random
from PyQt5 import QtCore
import sys


class gameFunctions():
    """ The game class that have the functionality of the game """

    def setNumbers(card1, card2, card1copy, card2copy):
        """ The function that generates numbers for player cards.
        setNumbers function receives card1 and card2 arrays which consist of the labels for corresponding places.
        Also, it takes two empty numpy array to copy card1 and card2 array for later use.
        The function generates number for cards and assigns them to corresponding location. 
        Then it shows generated numbers on the player cards.

        Syntax : setNumbers(card1, card2, card1copy, card2copy)

        Parameters :
        card1: An array of size (3,5) which consist of labels for player 1 card numbers.
        card2: An array of size (3,5) which consist of labels for player 2 card numbers.
        card1copy: An array of size (3,5) which consist of all zeros.
        card2copy: An array of size (3,5) which consist of all zeros.

        Returns:
        The function does not return anything.

        """
        card1_numbers = np.random.choice(
            np.arange(1, 91), replace=False, size=(3, 5))
        card2_numbers = np.random.choice(
            np.arange(1, 91), replace=False, size=(3, 5))  # generate a numpy array with a size of (3,5) in range (1, 91)

        for i in range(3):  # loop through each row
            card1_numbers[i].sort()
            card2_numbers[i].sort()  # sort each row of card in ascending order
            for j in range(5):  # loop through each number
                card1copy[i][j] = card1_numbers[i][j]
                # copy generated card numbers for later use
                card2copy[i][j] = card2_numbers[i][j]
                card1[i][j].setText(str(card1_numbers[i][j]))
                # Set generated number to corresponding UI element
                card2[i][j].setText(str(card2_numbers[i][j]))
                card1[i][j].raise_()
                card2[i][j].raise_()

    def pickStamp(restartButton, endMessage, player1, player2, bingoArray1, bingoArray2, stampArray1, stampArray2, pickedNumber, card1, card2, cardCopy1, cardCopy2, playerScoreLabel1, playerScoreLabel2):
        """ The function that put stamps when the picked number matches with a number in any player card.

        Syntax : pickStamp(restartButton, endMessage, player1, player2, bingoArray1, bingoArray2, stampArray1, stampArray2, pickedNumber, card1, card2, cardCopy1, cardCopy2, playerScoreLabel1, playerScoreLabel2)

        Parameters :
        restartButton: The UI element who is responsible to restart the game.
        endMessage: The UI element who is responsible to show end message to the user.
        player1: The UI element which shows the name of player 1.
        player2: The UI element which shows the name of player 2.
        bingoArray1: An array of UI elements which holds bingo icons for player 1.
        bingoArray2: An array of UI elements which holds bingo icons for player 2.
        stampArray1: An array of UI elements which consists of stamps for first card.
        stampArray2: An array of UI elements which consists of stamps for second card.
        pickedNumber: The UI element which shows the picked number which is chosen randomly from the bag.
        card1: An array of size (3,5) which consist of labels for player 1 card numbers.
        card2: An array of size (3,5) which consist of labels for player 2 card numbers.
        cardCopy1: A copy array card1 array.
        cardCopy2: A copy array card2 array.
        playerScoreLabel1: The UI element which shows the score of player 1.
        playerScoreLabel2: The UI element which shows the score of player 2.


        Returns:
        The function does not return anything.

        """
        for row, arr in enumerate(card1):  # loop through card1
            for i, val in enumerate(arr):  # loop through each row in card1
                # if the picked number is equal to any number on the row
                if int(pickedNumber.text()) == int(val.text()):
                    # show the corresponding stamp of the number
                    stampArray1[row][i].raise_()
                    cardCopy1[row][i] = cardCopy1[row][i] + 100
                    if(gameFunctions.checkBingo(cardCopy1, row)):  # check bingo for corresponding row
                        gameFunctions.updateScore(restartButton, playerScoreLabel1,
                                                  bingoArray1, player1, endMessage)  # update score of the corresponding player

        for row, arr in enumerate(card2):  # loop through card2
            for i, val in enumerate(arr):  # loop through each row in card2
                # if the picked number is equal to any number on the row
                if int(pickedNumber.text()) == int(val.text()):
                    # show the corresponding stamp of the number
                    stampArray2[row][i].raise_()
                    cardCopy2[row][i] = cardCopy2[row][i] + 100
                    if(gameFunctions.checkBingo(cardCopy2, row)):  # check bingo for corresponding row
                        gameFunctions.updateScore(restartButton, playerScoreLabel2,
                                                  bingoArray2, player2, endMessage)  # update score of the corresponding player

    def pickANumber(restartButton, endMessage, player1, player2, bag_count, bag, pickedNumber, stampArray1, stampArray2, card1, card2, cardCopy1, cardCopy2, bingoArray1, bingoArray2, playerScoreLabel1, playerScoreLabel2):
        """ The function that pick and remove randomly picked number from the bag and runs pickStamp function.

        Syntax : pickANumber(restartButton, endMessage, player1, player2, bag_count, bag, pickedNumber, stampArray1, stampArray2, card1, card2, cardCopy1, cardCopy2, bingoArray1, bingoArray2, playerScoreLabel1, playerScoreLabel2)

        Parameters :
        restartButton: The UI element who is responsible to restart the game.
        endMessage: The UI element who is responsible to show end message to the user.
        player1: The UI element which shows the name of player 1.
        player2: The UI element which shows the name of player 2.
        bag_count: The UI element which shows the number of left numbers in the bag.
        bag: A list of numbers from 1 to 90 which is initially generated by the UI class.
        pickedNumber: The UI element which shows the picked number which is chosen randomly from the bag.
        stampArray1: An array of UI elements which consists of stamps for first card.
        stampArray2: An array of UI elements which consists of stamps for second card.
        card1: An array of size (3,5) which consist of labels for player 1 card numbers.
        card2: An array of size (3,5) which consist of labels for player 2 card numbers.
        cardCopy1: A copy array card1 array.
        cardCopy2: A copy array card2 array.
        bingoArray1: An array of UI elements which holds bingo icons for player 1.
        bingoArray2: An array of UI elements which holds bingo icons for player 2.
        playerScoreLabel1: The UI element which shows the score of player 1.
        playerScoreLabel2: The UI element which shows the score of player 2.

        Returns:
        The function does not return anything.

        """

        randomNumber = random.choice(bag)  # pick a random number from the bag
        # display the picked number in the UI
        pickedNumber.setText(str(randomNumber))
        bag.remove(randomNumber)  # remove the picked number from the bag
        bag_count.setText(str(f"{len(bag)}/90"))
        bag_count.raise_()  # display the number of left numbers in the UI
        gameFunctions.pickStamp(restartButton, endMessage, player1, player2, bingoArray1, bingoArray2, stampArray1, stampArray2, pickedNumber,
                                card1, card2, cardCopy1, cardCopy2, playerScoreLabel1, playerScoreLabel2)  # pick stamp if the picked number matches with any of the number on the card

    def checkBingo(cardCopy, row):
        """ The function that checks bingo for given row.

        Syntax : checkBingo(cardCopy, row)

        Parameters :
        cardCopy: A copy array of the card which have +100 .
        row: Row number to check bingo.

        Returns:
        The function returns a boolean value.

        """
        bingo = True
        for i in cardCopy[row]:
            if i < 100:
                bingo = False
        return bingo

    def updateScore(restartButton, playerScoreLabel, bingoArray, playerName, endMessage):
        """ The function that updates the player score and end the game if any player wins.

        Syntax : updateScore(restartButton, playerScoreLabel, bingoArray, playerName, endMessage)

        Parameters :
        restartButton: The UI element who is responsible to restart the game.
        playerScoreLabel: The UI element which shows the score of given player.
        bingoArray: An array of UI elements which holds bingo icons for given player.
        playerName: The UI element which shows the name of given player.
        endMessage: The UI element who is responsible to show end message to the user.

        Returns:
        The function does not return anything.

        """
        player = int(playerScoreLabel.text())
        if player == 0:
            player = player + 10
            bingoArray[0].raise_()
        elif player == 10:
            player = player + 20
            bingoArray[1].raise_()
        elif player == 30:
            player = player + 40
            bingoArray[2].raise_()
            gameFunctions.endGame(playerName, endMessage,
                                  restartButton)  # end the game
        playerScoreLabel.setText(str(player))  # display player's updated score

    def endGame(playerName, endMessage, restartButton):
        """ The function that ends the game.

        Syntax : endGame(playerName, endMessage, restartButton)

        Parameters :
        playerName: The UI element which shows the name of given player.
        endMessage: The UI element who is responsible to show end message to the user.
        restartButton: The UI element who is responsible to restart the game.

        Returns:
        The function does not return anything.

        """
        endMessage.setInformativeText(
            f"{playerName.text()} Won !")  # inform the user about the winning player
        endMessage.exec_()
        restartButton.raise_()

    def restart():
        """ The function that restarts the game.

        Syntax : restart()

        Parameters :
        The function does not receive any parameter.

        Returns:
        The function does not return anything.

        """
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
