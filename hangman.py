hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]
num_wrong_guesses_allowed = len(hangman_parts)
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]

def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)



stored_name = input ("Enter your name ")
print("Hello, " + stored_name + ". It's time to play a game!")


find_word = "test"

def draw_guesses(letters_guessed, guess_word):
    for character in guess_word:
        if (character in letters_guessed):
            print (charcter)
        else (print " _ ")

errors = 0
guessed_letters = []

while errors < 6:
    guess = input("Enter a letter: ")
    guessed_letters.append(guess)
    print (guessed_letters)
    if guess.lower() in find_word:
        print("Good Job!")
    else:
        print("Congrats you failed at life!")
        errors = errors +1
        print ("Error count {}".format(errors))
        if errors >= 6:
            print ("Sorry, you lost the game. Please try again later.")
        draw_hangman(errors)





