'''
Program: project5p291.txt
Author: Alex Jones
Date: 11/21/2021
Purpose: Create a game where the software guesses a user's number between 1-100.
'''

from breezypythongui import *
import random

class GuessingGame(EasyFrame):
    """User thinks of a number between 1 and 100 and
    the program guesses the number."""
    
    
    
    def __init__(self):
        # Set up
        
        self.count = 1
        self.guess = random.randint(1, 100)
        self.lowerBound = 1
        self.upperBound = 100
        
        
        EasyFrame.__init__(self, "Guessing Game")
        
        # Formatting the guess
        self.guessLabel = self.addLabel(text = "Current Guess",
                                        row = 0, column = 0)
        self.guessText = self.addTextArea(text = str(self.guess),
                                                     row = 0, column = 1)
        
        # Formatting the buttons
        self.tooSmall = self.addButton(text = "Too Small", row = 1, column = 0,
                                       command = self.higherGuess)
        self.tooLarge = self.addButton(text = "Too Large", row = 1, column = 1,
                                       command = self.lowerGuess)
        self.correct = self.addButton(text = "Correct", row = 1, column = 2,
                                      command = self.correctGuess)
        self.newGame = self.addButton(text = "New Game", row = 1, column = 3,
                                      state = "disabled", command = self.newGame)
                                        
    def lowerGuess(self):
        """Processes a lower guess for the program."""
        self.count += 1
        self.upperBound = self.guess - 1
        self.guess = random.randint(self.lowerBound, self.upperBound)
        self.guessText.setText(str(self.guess))
        
    def higherGuess(self):
        """Processes a higher guess for the program."""
        self.count += 1
        self.lowerBound = self.guess + 1
        self.guess = random.randint(self.lowerBound, self.upperBound)
        self.guessText.setText(str(self.guess))
        
    def correctGuess(self):
        """Processes a correct guess"""
        self.guessLabel["text"] = ""
        self.guessText.setText("I guessed it in "+str(self.count)+" tries!")
        self.tooSmall["state"] = "disabled"
        self.tooLarge["state"] = "disabled"
        self.correct["state"] = "disabled"
        self.newGame["state"] = "normal"
        
    def newGame(self):
        """Set GUI and data to original states"""
        self.guess = random.randint(1, 100)
        self.count = 0
        self.lowerBound = 1
        self.UpperBound = 100
        self.guessLabel["text"] = "Current Guess"
        self.guessText.setText(str(self.guess))
        self.tooSmall["state"] = "normal"
        self.tooLarge["state"] = "normal"
        self.correct["state"] = "normal"
        self.newGame["state"] = "disabled"
        

        
def main():
    """Instantiates the the window"""
    GuessingGame().mainloop()
    
if __name__ == "__main__":
    main()
