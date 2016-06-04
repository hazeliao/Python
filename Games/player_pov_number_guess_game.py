import math
import re
import random


def mainGame():
    print("Please enter 2 values for range:")
    numberChecking = True
    while ( numberChecking ):
        try:
            numberRange = input()
            minNumber, maxNumber  = [int(x)for x in sorted(re.findall('\d+', numberRange)) ]
            break
        except ValueError:
            print("Input the right numbers please!")
            continue
        numberChecking = False
        
    tries = math.ceil(math.log2(maxNumber-minNumber))
    goalNumber = random.randint(minNumber, maxNumber)
    print( "Guess a number:" )
    while(True):
        if tries == 0:
            print("Ran out of tries!")
            break

        checkingInput = True
        while ( checkingInput ):
            try:
                guessedNumber = int(input())
            except ValueError:
                print("Input only numbers please!")
                continue

            if minNumber < guessedNumber <= maxNumber :
                checkingInput = False
            else:
                print( "Your number is over or under the max / min limit!" )
                print( "Please type a valid number between ", minNumber, " and ", maxNumber, ": " )               
            
        if guessedNumber == goalNumber :
            print("That's right! That was my number!")
            break        
        else:
            if guessedNumber > goalNumber :
                print("This number is higher than the number I have in mind! Next try?")
            else:
                print("This number is lower than the number I have in mind! Next try?")
            tries -= 1
            print("You have ", tries, " tries left")
    print("Play again? y/n")
    checkinginput = True
    while ( checkinginput ):
        playAgain = input()
        if playAgain.lower() == 'y':
            mainGame()
        elif playAgain.lower() == 'n':
            print("Hope you enjoy the game!")
            quit
        else:
            print("please write only y or n")
  
       
mainGame()     
        
    
