name = ""


def game_intro():
    """
    TheIntro to the game, Introducing to the player
    and asks for name
    """
    global name
    name = input("Unless your name is Deadpool.."
                 "Enter your name here:\n").strip().lower()

    if name == "":
        print("Any name will do..")
        game_intro()
    elif name == "Deadpool".strip().lower():
        print("Ooohkay, go on then 'Mr. Pool'")
    else:
        print(f"\n Welcome {name} to the quiz all about Deadpool!\n")
    new_game()


def new_game():
    """
    The beginning of the game
    """
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-|-|-|-|-|-|-|-")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = ''
        possible_answers = ['A', 'B', 'C']
        while guess not in possible_answers:
            guess = input("Try (A, B, or C)").strip().upper()
            if guess == '':
                print('Hey you need to enter something not just spaces')
                continue
            if guess not in possible_answers:
                print("Hey you need to enter something like")
                print("A, B or C... Wake up!")
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
    print("You manged to get: "+str(score)+"%")
    play_again()


def play_again():
    """
    An option to restart the quiz
    """
    response = ''
    possible_reponses = ['YES', 'NO']
    while response not in possible_reponses:
        response = input("Wanna try again? (YES or NO): ").strip().upper()
        if response == '':
            print('Hey you need to enter something not just spaces')
            continue
        if response not in possible_reponses:
            print('Hey you need to enter something like YES, NO .... Wake up!')

    if response == "YES":
        new_game()
    else:
        print("Guess you aren't nerdy enough.. Thanks for playing!")


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
options = [
    ["A: Richard Webber", "B: Wade Wilson", "C: Slade Wilson"],
    ["A: 2000", "B: 2016", "C: 1991"],
    ["A: 2000", "B: 2016", "C: 2018"],
    ["A: Rogue", "B: Storm", "C: Vanessa"],
    ["A: Cows", "B: Apples", "C: Driving"],
    ["A: Sherlock Holmes", "B: Moby Dick", "C: All of the above"],
    ["A: USA", "B: UK", "C: Canada"],
    ["A: X-Men Origins: Wolverine", "B: Deadpool: 1", "C: Deadpool: 2"],
]
game_intro()

