# # Hangman Game
# The instructions below will help you to create your own hangman game. Answers (don't cheat unless you have to!) are
#  provided in the bonus_hangman_answers.py file in this directory.

# First, we import the libraries we need: requests and random. Random comes with the standard python libraries, and
#  can be used to generate pseudo-random numbers, or choose pseudo-randomly from lists of objects.
import random
from lib import hangman

# This is a URL for 1000 most commonly used words in the english language.
url = 'https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt'

# Let's start out with a class, HangmanGame
class HangmanGame:
    def __init__(self):
        # First, we need to store our 1000 words.
        self.wordlist = []
        # Problem 1: write a requests function call to get this data.




        # Problem 2: Split the response.text into a list of words. You'll want to split on a newline character, '\n'
        #   Then, add each word to self.wordlist. Strip off any whitespace that may have sneaked in there.




        # Check this file for cool ASCII art.
        self.art = libhangman.art
        # We only have so much art
        self.max_guesses = len(self.art) - 1
        # Set up things to be used later
        self.current_word = None
        self.guesses = []
        self.wrong_guesses = []
        self.right_guesses = []
        self.miss_count = 0
        # Reset the game so it's ready to play.
        self.reset()

    # this function resets everything so we can play again.
    def reset(self):
        # Pick a word to start with
        self.current_word = self.get_word()
        # Clear the guesses lists
        self.guesses.clear()
        self.wrong_guesses.clear()
        self.right_guesses.clear()
        # Counters to store number of guesses
        self.miss_count = 0

    # We can use random.choice() to select a random word from the wordlist.
    def get_word(self):
        return random.choice(self.wordlist)

    # define a function related to the progress of the game
    def display_status(self):
        # This is the word we will print.
        display_word = ""
        # Problem 3: We need to substitute underscore characters for any letters that haven't been guessed.
        #  Remember you can loop through each letter of a string just like a list.
        #  Don't forget that you need to handle lowercase vs uppercase. 'A' does not equal 'a'!





        # Then we print out the word.
        print(f"Word: {display_word.upper()}")

        # Show the wrong guesses
        if len(self.wrong_guesses) > 0:
            # The .join() string method combines the elements of a list, with the string it was called from in between
            # called on the string object " ", it will combine the wrong guesses with a single space in between.
            print(f"Wrong guesses: {' '.join(self.wrong_guesses).upper()}")

        # Show the art. The art variable is a list of lists of strings. Each list of strings is one frame of the image
        #  The frames are ordered in the list in order of increasing bad guesses. Each wrong guess takes us on to the
        #  next frame in the picture.
        for line in self.art[len(self.wrong_guesses)]:
            print(line)

    def guessed_word(self):
        # Ok, so this is a little complex. A set is a special datastructure that can only hold one of
        #  each object. As such, we can see if all the letters in the word are also in the guesses.
        return set(self.current_word.upper()) == set(self.right_guesses)

    def play_again(self):
        while True:
            # This loop allows us to make sure that valid data is entered.
            #  It will loop endlessly until something is returned out of the function, thereby ending the loop.
            # The input() method allows us to get text from the user. They enter this at the Python Console.
            play_again_input = input("Play again? [Y/N]: ").upper()
            if (play_again_input in ['Y', 'YE', 'YES', 'YEAH']):
                return True
            if (play_again_input in ['N', 'NO', 'NAH', 'NOPE']):
                return False
            print('Invalid choice. Try again!')

    def get_input(self):
        # this loop is similar to the first, but instead of returning from inside the if statements, it skips the end
        #   of the loop with a 'continue' so that the value doesn't egt returned.
        while True:
            guess = input("Write a letter: ").upper()
            # Check to make sure it's only 1 character, and is a letter
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid guess. Try again.')
                continue
            # Check to make sure it's not a repeated guess
            if guess in self.guesses:
                print('You already guessed that! Try again.')
                continue
            # If we haven't hit a 'continue' by now, we'll return the letter.
            return guess

    def play(self):
        # These variables help us manage the state of the game.
        # This first one tells us if we're done or not.
        continuing = True
        # This one tells us whether current game has ended.
        ended = 0
        # This loop will continue the game loop until the player ends it.
        while continuing:
            # This allows us to exit the loop cleanly.
            try:
                # Problem 4: Game Logic. I have the overall structure of what we need to do to make the game work.
                #  Fill in the appropriate method calls:
                # First, we print out the status of the game

                # Get a new letter guess
                new_letter = None
                # Add it to our guesses list

                # Check to see if the guess is correct
                if ... :
                    # It's correct, so we will add it to the correct list

                    # We check to see if they've guessed the word.
                    if ... :
                        print('You Win!')
                        # Set our ended variable up to indicate the end of the game.
                        ended = True
                    else:
                        print('Good Guess!')
                else:
                    # If it's wrong, we'll add it to the wrong guesses.
                    self.wrong_guesses.append(new_letter)
                    # Check to see if they've lost the game
                    if len(self.wrong_guesses) == self.max_guesses:
                        print(f'You Lose! The word was {self.current_word}')
                        ended = True
                    else:
                        print('Nope!')
                if (ended):
                    # Figure out if we need to play again
                    continuing = self.play_again()
                    if continuing:
                        # Reset the game
                        self.reset()
                        # Make sure we reset the game state.
                        ended = False
            # This handles any unexpected errors or exits.
            except:
                print("Exiting...")
                continuing = False


# Finally, we have this little thing. This allows us to run this file on its own.
#  Since the code above will only create the class, we need this code to actually create an instance of the class
#  and run the play() method.
# You could do this from a separate file by importing bonus_hangman, and running these final two lines as well.
# To do this from the Python Console, type:
# >>> import bonus_hangman
# >>> game = bonus_hangman.HangmanGame()
# >>> game.play()
if __name__ == '__main__':
    # Remember, this runs __init__()
    game = HangmanGame()
    game.play()

# Have fun playing the game! See if you can add more features or improve the art!