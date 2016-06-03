word_list = ["anathema", "claire", "Amanda"]

def inititalize(word_list):
    for word in word_list:
        if not start_new_game(word):
            break
    print( "The program stops executing." )


def obfuscate(word, letters_guessed):
    word_in_lower = word.lower()
    current_word_result = ""
    found_match = False
    for i in range(len(word_in_lower)):
        for a in range(len(letters_guessed)):
            if word_in_lower[i] == letters_guessed[a]:
                found_match = True
                current_word_result += letters_guessed[a].upper()
        if not found_match:
            current_word_result += "_"
        found_match = False

    return current_word_result

def start_new_game(word):
    letters_guessed = ""
    print ("Word: " + '_'*len(word)) 
    was_successfull = False
    letters = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
    i = 0
    while ( i < 10):
        print("Tries left: ", 10-(i), " Guess a letter:")
        x = input()
        x = x.lower()
        if ( len( x ) > 1 or letters_guessed.upper().find( x.upper() ) == -1 and letters.find ( x.upper()) == -1):
            print("Wrong input! Please write only one letter! ")
            continue
        if ( letters_guessed.upper().find( x.upper() ) != -1):
            print("The letter " + x + " was already guessed! ")
            continue

        letters = letters.replace(x.upper(), '')
        letters_guessed += x
           
        result_word = obfuscate( word, letters_guessed )
        print( result_word )
        if result_word.lower() == word.lower():
            print("You guessed the word correctly!")
            was_successfull = True
            
        print( "Letters remaining: ", letters.upper() )
        if word.lower().find(x.lower()) == -1 :
            i += 1
            if i == 10 :
                print ("Out of tries!")
        if was_successfull:
            break

    print( "Do you want to play again? (y)/(n)")
    x = input()
    if x.lower() == "y":
        return True
    else:
        return False

inititalize( word_list )
