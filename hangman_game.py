#Creating a Hangman Game in Python
#In this game you need to guess names of different fruits and if your guess is right, you will win the game else you will lose it.
#You will be given 10 chances to make guesses.

#Importing random module for selecting different fruit name each time form the list.
import random    

def hangman():
    #list of fruits
    word_list = ['apple','mango','pineapple','banana','orange']
    word = random.choice(word_list)
    turns = 10
    guessmade = ""
    #checking the validation of the input by user
    valid = set('abcdefghijklmnopqrstuvwxyz123')
    
    while len(word)>0:
        user_word = ""
        
        for letter in word:
            if letter in guessmade:
                user_word = user_word + letter
            else:
                user_word = user_word + " _ "
            
        if user_word == word:
            print(user_word)
            print("You Won!!")
            break
        
        print("Guess the letter",user_word)
        guess = input()
        
        if guess in valid:
            guessmade = guessmade + guess
        else:
            print("Enter valid character")
            guess = input()
            
        if guess not in word:
            turns = turns - 1
            
            if turns == 9:
                print("9 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
            if turns == 8:
                print("8 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
            if turns == 7:
                print("7 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
            if turns == 6:
                print("6 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
            if turns ==5:
                print("5 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
            if turns == 4:
                print("4 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
            if turns == 3:
                print("3 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
            if turns == 2:
                print("2 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
            if turns == 1:
                print("1 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
            if turns == 0:
                print("0 turns left")
                print("_ _ _ _ _ _ _ _ _ _")
                print("You loose")
    
    
    
print("_ _ _ _ _ _ _ _ _ _")
print("Try to guess the word in 10 attempts")
hangman()

