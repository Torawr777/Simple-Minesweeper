from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MS_model import * 

class MS_window(QMainWindow):
    def __init__(self):
        super(MS_window, self).__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        layout.setSpacing(0) 
        widget.setLayout(layout)

        self.state = QLabel("0")
        font = QFont("Arial", 20, QFont.Bold)
        self.state.setFont(font)
        self.state.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.state.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.state)
        self.buttons = []


        grid = QGridLayout()
        for i in range(100):
            size = QSize(50, 50)
            button = QPushButton()
            button.setFixedSize(size)

            button.clicked.connect(self.buttonClicked)
            self.buttons.append(button)

            # 10x10 grid 
            row = i // 10
            col = i % 10

            # Keep track of button position
            button.setProperty("myRow", row)
            button.setProperty("myCol", col)

            grid.addWidget(self.buttons[i], row, col)
        layout.addLayout(grid)

        menu = self.menuBar().addMenu("&Menu")
        newAct = QAction("&New Game", self, shortcut=QKeySequence.New, triggered=self.newGame)

        menu.addAction(newAct)
        menu.addSeparator()
        quitAct = QAction("E&xit", self, shortcut=QKeySequence.Quit, triggered=self.close)
        menu.addAction(quitAct)

        self.setWindowTitle("Minesweeper Demo")
        self.model = MS_model()
        self.newGame

    def newGame(self):
        print("Starting a new game!")
        count = self.model.getMoveCount(0)
        self.state.setText(str(count))

        # 1) Unlock all the buttons
        for button in self.buttons:
            button.setEnabled(True)
            button.setText("")

        # 2) Have model generate new map
        self.model.newGame()

       
    def buttonClicked(self):
        clicked = self.sender()

        # Coordinates of clicked button
        row = clicked.property("myRow")
        col = clicked.property("myCol")

        # 1) Disable the button
        clicked.setEnabled(False)

        # 2) Tell model about button clicked 
        adj = self.model.getSquare(row, col)
        count = self.model.getMoveCount(1)
        
        # "Reveal" square(bomb or not, adj count)
        clicked.setText(str(adj))
   
        # 3) Update display (bomb or not? with adj bomb counter)
        if self.model.getGameState(row, col) == -1:
            self.state.setText("You got nuked in " + str(count) + " move(s).")

        elif self.model.getGameState(row, col) == 1:
            self.state.setText("You've escaped in " + str(count) + " moves.")

        else:
            self.state.setText(str(count)) 
            
            

