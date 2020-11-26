# This is the main file to start the game
# You may add any additional modules and other files you wish
import yaml
import random
from words import word_list

def get_words():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completeness = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 8
    with open('inscription.yaml', 'r') as saved_file:
        print(yaml.load(saved_file))
    print("Let's take a journey with Hangman!")
    print(hangman_stages(lives)) 
    print(word_completeness)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Give us your letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(guess, "is not gonna work again.")
            elif guess not in word:
                print("Wrong answear!")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print("You are a lucky man,", guess, "is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completeness)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completeness = "".join(word_as_list)
                if "_" not in word_completeness:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha:
            if guess in guessed_words:
                print("You already try this luck", guess)
            elif guess != word:
                print(guess,"is not the word. Learn english!")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completeness = word
        else:
           print("Not quite, choose wisely!")
        print(hangman_stages(lives))
        print(word_completeness)
        print("\n")
    if  guessed: 
        print("Congratulations, you've made it!")
    else:
        print("Do or do not, there is not try. The word was " + word + ". ")    



def hangman_stages(lives):
    stages = [  """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    / \\
                    -
                """,
                """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |    /
                    -
                """,
                """
                    -------
                    |     |
                    |     O
                    |    \\|/
                    |     |
                    |
                    -
                """,
                """
                    -------
                    |     |
                    |     O
                    |    \\|
                    |     |
                    |
                    -
                """,
                """
                    -------
                    |     |
                    |     O
                    |     |
                    |     |
                    |
                    -
                """,
                """
                    -------
                    |     |
                    |     O
                    |
                    |
                    |
                    -
                """,
                """
                    -------
                    |     |
                    |
                    |
                    |
                    |
                    -
                """,
                """
                    |
                    |
                    |
                    |
                    |
                    -
                """,
                """





                    -
                """    
     ]
    return stages[lives]



def main():
    word = get_words()
    play(word)
    while input("Do you want rematch ? (Y/N) ").upper() == "Y":
        print("\n")
        word = get_words()
        play(word)



if __name__ == "__main__":
    main()