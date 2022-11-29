def new_game():
    """
    The start of the Game, Introducing to the player
    """
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Try (A, B, or C)").strip().lower()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    """
    A Function that will check the correct answers for the User
    """
    if answer == guess:
        print("Nailed It!!!")
        return 1
    else:
        print("YOU are WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    """
    A score card for the player to keep track with
    """
    print("_>_>_>_>_>_>")
    print("Scores")
    print("_>_>_>_>_>_>")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print(f"You manged to get: "+str(score)+"%")


def play_again():
    """
    An option to restart the quiz
    """
    response = input("Wanna try again? (YES or NO): ")
    response = response.strip().lower()

    if response == "YES":
        return True
    else:
        return False


"""
These are the quiz Questions inside a dictionary
"""

questions = {
    "What is Deadpools real name?": "B",
    "When was the first Deadpool comic released": "C",
    "When was the first Deadpool Movie released": "B",
    "Who is Deadpools main Romance/girlfriend in the Movies": "C",
    "Deadpool has bovinophobia, which is the fear of what..?": "A",
    "What Fictional Character has Deadpool killed in the comics": "C",
    "Where is Deadpool from?": "C",
    "What Movie was the character first played by Ryan Reynolds?": "A"
    }


"""
These are the possible options to the quiz questions
"""

options = [["A: Richard Webber","B: Wade Wilson","C: Slade Wilson"],
    ["A: 2000", "B: 2016", "C: 1991"],
    ["A: 2000", "B: 2016", "C: 2018"],
    ["A: Rogue", "B: Storm", "C: Vanessa"],
    ["A: Cows", "B: Apples", "C: Driving"],
    ["A: Sherlock Holmes", "B: Moby Dick", "C: All of the above"],
    ["A: USA", "B: UK", "C: Canada"],
    ["A: X-Men Origins: Wolverine", "B: Deadpool: 1", "C: Deadpool: 2"]]


new_game()

while play_again():
    new_game()

print("Guess you aren't nerdy enough.")