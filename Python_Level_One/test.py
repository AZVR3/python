import random

def get_guess():
    '''
    Asks for the number guess and transforms the string to a list.
    '''
    return list(input("What is your guess?"))

def generate_code():
    '''
    generates a 3 digit list for the code
    '''
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code,userGuess):
    '''
    Takes in a user guess and code then compares the numbers in a loop and
    creates a list of clues according to the matching parameters.
    '''
    if userGuess == code:
        return "CODE CRACKED"

    clues = []


    for ind,num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

# Run Game
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")


secretCode = generate_code()
print("Code has been generated, please guess a 3 digit number")



clueReport = []


while clueReport != "CODE CRACKED":


    guess = get_guess()

    clueReport = generate_clues(guess,secretCode)
    print("Here is the result of your guess:")
    for clue in clueReport:
        print(clue)
