import math
import re


def mainGame():
    print("What range is your number in:")
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
    
    
    while(True):
        guessedNumber = (minNumber + maxNumber)//2
        if tries == 0:
            print("Ran out of tries!")
            break
        print("Is your number ", guessedNumber, "?")      
        goalNumber = input()
        low = goalNumber.lower()
        if low == "y":
                print("Woah, that  was tricky!")
                break
        elif low == "h" :
                minNumber = guessedNumber + 1
                tries -= 1
        elif low == "l":
                maxNumber = guessedNumber
                tries -= 1                
        else:                
            print("Input answer please!")
            continue
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
        
