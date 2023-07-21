import random

class MS_model:
    def __init__(self):
        self.newGame()

    def newGame(self):
        # 1) Initialize game grid
        self.grid = [[0]*(10) for i in range(10)] #10x10 grid initialized to 0

        # 2) Add appropriate number of bombs (10 total)
        for i in range(10): 
            while True: # Loop until 10 bombs are actually placed
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                if(self.grid[row][col] == 0):
                    self.grid[row][col] = 1 # Set the bomb(equals 1)
                    break
      
      
    def getSquare(self, row, col):
        # Returns current state of an indicated square
        # Revealed or not, adj. bomb count)
        bombCount = 0
        if self.grid[row][col] == 1:
            return "X" 
        elif self.grid[row][col] == 0:
            # Loop through coordinates adjacent to clicked square
            for x in range(-1,1):
                for y in range(-1,1):
                    if (self.inside(x+row, y+col) == True) and (self.grid[x+row][y+col] == 1):
                        bombCount += 1
            return bombCount
            


    # Check if adjacent squares are in the map
    def inside(self, x, y):
        if x >= 0 and x < 10 and y >= 0 and y < 10:
            return True
        return False
        
    
    def getMoveCount(self, count):
        # Returns number of moves made
        # Using class attribute for "static" variable
        if not hasattr(MS_model, "counter"):
            MS_model.counter = 0 #initialize it if it doesn't exist 

        if count == 1: # increment counter
            MS_model.counter += 1
        elif count == 0: # reset counter
            MS_model.counter = 0
        return MS_model.counter
        

    def getGameState(self, row, col):
        # Indicates current state of the game (won, lost, in progress)
        # -1 = Loss
		#  0 = in progress
		#  1 = win
        if self.grid[row][col] == 1: # Loss
            return -1
        return 0 # In progress
        
        