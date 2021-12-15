# Game of Thrones Project

# For this project, I'm building a Fill-in-the-Blanks quiz.
# This quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.


def gameDifficulty():

    ''' This function prompts user to select difficutly level.
    No arg.

    Returns: A string gameDifficulty and an integer quantityOfGuesses

    '''
    userSelect = input('Please select your difficulty. Easy, Medium or Hard: ')

    if userSelect == 'Easy' or userSelect == 'easy' or userSelect == 'E' or userSelect == 'e':
        gameDifficulty = 'Easy'
        return gameDifficulty

    elif userSelect == 'Medium' or userSelect == 'medium' or userSelect == 'M' or userSelect=='m':
        gameDifficulty = 'Medium'
        return gameDifficulty


    elif userSelect == 'Hard' or userSelect == 'hard' or  userSelect == 'H' or userSelect == 'h':
        gameDifficulty = 'Hard'
        return gameDifficulty

    else:
        print ('Invalid choice, Please pick a valid choice')
        return None

def gameGuesses(gameDifficulty):
    ''' Function takes game difficulty as input and returns the corresponding number of guesses as output
        Arg: gameDifficulty
        Return: quantityOfGuesses
    '''
    if gameDifficulty == 'Easy':
            quantityOfGuesses = 4
            print ("You have chosen " + gameDifficulty + "!\n")
            print ("You will get " + str(quantityOfGuesses) + " guesses per problem\n")
            return quantityOfGuesses

    elif gameDifficulty == 'Medium':
            quantityOfGuesses = 2
            print ("You have chosen " + gameDifficulty + "!\n")
            print ("You will get " + str(quantityOfGuesses) + " guesses per problem\n")
            return quantityOfGuesses

    elif gameDifficulty == 'Hard':
            quantityOfGuesses = 1
            print ("You have chosen " + gameDifficulty + "!\n")
            print ("You will get " + str(quantityOfGuesses) + " guesses per problem\n")
            return quantityOfGuesses

    else:
            print ('Invalid choice, Please pick a valid choice')
            return None


def gameQuestion(gameDifficulty):
    ''' This fuction takes the gameDifficulty and returns the appropriate question
        Arg: gameDifficulty
        Returns: gameQuestion
    '''
    if gameDifficulty == 'Easy':
        gameQuestion = '''Daenerys is a member of House ___1___. The name of her husband is ___2___.\nGeographically, House Stark is located ___3___ of King's Landing.\nNed Stark's wife is named ___4___ Stark.'''
        return gameQuestion

    elif gameDifficulty == 'Medium':
        gameQuestion = '''Hear me Roar! are the words for House ___1___.\nThey have a ___2___ as their sigil.\nThe surname given to bastards in Dorne is ___3___.\nGregor of House Clegane is also know as The ___4___ .'''
        return gameQuestion

    elif gameDifficulty == 'Hard':
        gameQuestion = '''___1___ Baratheon is the youngest of the Baratheon brothers.\nSansa Stark's first marraige was to ___2___ Baratheon.\nSer Ilyn ___3___ was the one who beheaded Ned Stark.\nSamwell Tarly traveled to ___4___ to become a maester.'''
        return gameQuestion
    else:
        return 'Error'

def gameAnswer(gameDifficulty):

    ''' This fuction takes the gameDifficulty and returns the appropriate question
            Arg: gameDifficulty
            Returns: gameSolution
    '''

    if gameDifficulty == 'Easy':
        gameSolution = ['Targaryen','Drogo','North','Catalyn']
        return gameSolution

    elif gameDifficulty == 'Medium':
        gameSolution = ['Lannister','Lion','Sand','Mountain']
        return gameSolution

    elif gameDifficulty == 'Hard':
        gameSolution = ['Renly','Joffery','Payne','Oldtown']
        return gameSolution
    else:
        return 'Error'

def gameCheck(qDifficulty,qGuesses,qTextList,qSolution):

    ''' Function logically checks users answers
        Arg: qDifficulty,qGuesses,qTextList,qSolution
        Returns: None
    '''
    emptySpaceNumber = 0
    currentGuesses = 0
    quizPlaceHolder = ['___1___','___2___','___3___','___4___']
    counter = 0
    qCounter = len(qSolution) #Keeps track of when and how many times the user has solved problems.

    while (counter < qCounter) and (currentGuesses < qGuesses):
        print ("The current paragraph reads as such:\n")
        print (qTextList)
        userGuess = input ("\nWhat should be substituted in for  " + quizPlaceHolder[emptySpaceNumber])

        if userGuess == qSolution[emptySpaceNumber] or userGuess == qSolution[emptySpaceNumber].lower() or userGuess == qSolution[emptySpaceNumber].upper(): #Allows lower and upper case user entries
            print ("\nCorrect!\n")
            qTextList = qTextList.replace(quizPlaceHolder[emptySpaceNumber], qSolution[emptySpaceNumber])
            emptySpaceNumber += 1
            currentGuesses = 0 #Resets currentGuesses
            counter += 1
        else:
            currentGuesses += 1
            print ("\nIncorrect. You have " + str(qGuesses - currentGuesses) + ' guesse(s) left\n')


def startGame():
    """Function starts the game and calls all sub functions
        No args.
    """

#Welcome Statement
    print ('\nWelcome Game of Thrones fan. Just how well do you know Game Of Thrones?\n')

    qDifficulty = gameDifficulty()

    qGuesses = gameGuesses(qDifficulty)

    qTextList = gameQuestion(qDifficulty)

    qSolution = gameAnswer(qDifficulty)

    gameCheck(qDifficulty,qGuesses,qTextList,qSolution)


startGame() #Begins Game


# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?
