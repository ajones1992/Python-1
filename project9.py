'''
Program: Giving the Sum and Average of Inputs
Date: 10/02/21
Author: Alex Jones
Purpose: Take inputs and return the sum and average of the inputs
'''

def sumOfInputs():
""" Receive inputs and return the sum and average of the inputs. """
    inputQuant = 0
    inputSum = 0
    inputReceiver = input("Type in values with spaces between and press enter to finish. ")
    
    numList = inputReceiver.split()
    for i in numList:
        inputSum += int(i)
        inputQuant += 1
        
    inputAv = inputSum / inputQuant
    print("Your total is " + str(inputSum) + ". Your average is " + str(inputAv) + ".")
    
sumOfInputs()