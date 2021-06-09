# Tombala Game with PyQt5

The aim of this project is to develop a bingo game with Python and Qt Designer. <br/>
Qt Designer is used to generate Python code from designed user interface.
See the source code in <a href="https://github.com/aturancetin/tombala-pyqt5">Github</a>

## Dependencies

Please install "PyQt5" and "numpy" before you run the project .

## How to run ?

Go into the project directory and give this command in the terminal;

```bash
python3 tombala.py
```

## How to play ?

In order to start the game press the PLAY and then INITIALIZE CARDS button. Then start playing simply by picking number from the bag with pressing PICK A NUMBER button. When the user presses PICK A NUMBER button, program checks for both players if the picked number matches with the numbers of the cards that players have been playing with. If so, stamps are put to the corresponding locations. When all of the stamps of a row are put, player has a bingo. Players take 10 points for first bingo, 20 points for second bingo and 40 points for third bingo. Player who reaches to 70 points, win the game.
