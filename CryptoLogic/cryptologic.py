from random import shuffle
from random import randint

def main():

    inputFile = open("wordlist.txt")

    list_secret_word = []
    player_guesses = []
    a = 0

     

    line = inputFile.readline()

    while(len(line) > 0):
        line = line.strip()
        
        list_secret_word.append(line)

        line = inputFile.readline()

    #print(secret_word_list) 

    secret = get_next_word(list_secret_word)

    scrambled_word = scramble_word(secret)

    gameWord = print_word(secret)

    guessWord = print_word(scrambled_word)

    

    print("Welcome to Crypto-Logic!")
    print("Try to unscramble the following word!")
    print(guessWord)

    gameOver = False
    s = 0

    while(not gameOver):
        b = input("Please enter a guess. ").upper()
        if(b == secret[s]):
            player_guesses.append(b)
            currentProgress = print_word(player_guesses)
            print(guessWord)
            print(currentProgress)
            print("Number of incorrect guesses: " + str(a))
            if(currentProgress == gameWord):
                print(guessWord)
                print(gameWord)
                print("You have unscrambled the word!")
                print("You had " + str(a) + " incorrect guess(es).")
                input("Press ENTER to exit the game.")
                gameOver = True   
            s += 1
        elif(b != secret[s]):
            a += 1
            currentProgress = print_word(player_guesses)
            print(guessWord)
            print(currentProgress)
            print("Number of incorrect guesses: " + str(a))
            
    inputFile.close()

def get_next_word(list_secret_word):

        x = list_secret_word[randint(0,299)]
        y = x.upper()
        list_secret_word.remove(x)
        word = list(y)

        return word

def scramble_word(secret):

    scramble = list(secret)
    shuffle(scramble)
    
    

    return scramble

def print_word(list):

    nonList_secret = ''.join(list)

    return nonList_secret
    

    
    

    




main()

