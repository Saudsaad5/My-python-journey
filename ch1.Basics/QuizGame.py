# creating a Tuples for questions, options, and answers key
questions =           ("How many elements are in the periodic table?: ", 
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")
# this Tuple is 2D
options =          (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers =          ("C", "D", "A", "A", "B")
# this list will be used to store user answers
guesses = []
score = 0
question_num = 0

# to print the questions
for question in questions:
    print("----------------------")
    print(question)
    # to print the options
    # the index question_num is 0 from the var above
    for option in options[question_num]:
        print(option)
    # here we ask the user to enter his guess
    # used .upper() to make the input an upper case
    guess = input("Enter (A, B, C, D): ").upper()
    # we store his answer in the list
    guesses.append(guess)
    # here we compare the user guess to our answers Tuple
    if guess == answers[question_num]:
        # score is alos a var = 0 
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        # to show the user the correct answer
        print(f"{answers[question_num]} is the correct answer")
    # to update the question number
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

# this will print the right answers
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

# this will print the user guesses from the list
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# it will calc the score based on the user answers
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")