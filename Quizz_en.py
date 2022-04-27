#coding=utf-8


phrases_gaps_answers = {
    "easy": {
        "phrases": "The __0__ is always __1__ on the other __2__ of the __3__.",
        "gaps": ["__0__", "__1__", "__2__", "__3__"],
        "answers": ["grass", "greener", "side", "fence"]
    },
    "medium": {
        "phrases": "Imagine __0__ the people livin'__1__ in peace. You may __2__ I'm a __3__ but i'm not the only...",
        "gaps": ["__0__", "__1__", "__2__", "__3__"],
        "answers": ["all", "life", "say", "dreamer"]
    },
    "difficult": {
        "phrases": "The __0__ of the hypotenuse side is equal to the __1__ of __2__ of the other two __3__",
        "gaps": ["__0__", "__1__", "__2__", "__3__"],
        "answers": ["square", "sum", "squares", "sides"]
    }
}
levels = ["easy", "medium", "difficult"]

options_of_chances_quantity = range(1,11)

last_chance = 1

def presentation():
    """
    Present the game
    """
    print ("\nWelcome!!!")
    print ("In this game, a phrase with four gaps, which you have to complete, will be displayed.")
    print ("Choose the difficulty level and the number of attempts to complete it\n")


def select_level():
    """
    Ask the user what is the desired level, check if the answer
    is valid and, if not, inform the user and ask again.
    Returns:
        (string) level "easy", "medium", "difficult"
    """
    level = input(("\nEscolha um nível de dificuldade: (easy | medium | difficult): ")).lower()
    while  level not in levels:
            level = input("\nThe level was not entered correctly. Choose from (easy | medium | difficult): ").lower()
    print ("\nThe level selected is: " + level + "\n")
    return level

def select_number_of_chances():
    """
    Ask the user what is the desired number of chances, check if the answer
    is valid and, if not, inform the user and ask again.
    Returns:
        (int) chances "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
    """

    while True:
        try:
            chances = int(input("Enter the number of chances (between 1 and 10) you want to have: "))
            if chances not in options_of_chances_quantity:
                raise ValueError
        except ValueError:
            print("You did not enter a number or the number is not within the range 1 to 10\n")
        else:
            break

    return chances

def load_phrases_gaps_response(level):
    """
    Load the phrases, gaps, and answers to the corresponding level.
    Args:
        level (string): nível "easy", "medium", "difficult".
    Returns:
        (string) phrases with gaps
        (list) List com as gaps.
        (list) List with the answers.
    """
    phrases = phrases_gaps_answers[level]["phrases"]
    gaps = phrases_gaps_answers[level]["gaps"]
    answers = phrases_gaps_answers[level]["answers"]
    return phrases, gaps, answers

def play(chances, phrases, gaps, answers):
    """
    Display the phrases to the user, ask for the answer regarding a gap and
    compare with the correct answer.
    If the answer is wrong, it decreases the number of chances, displays a message of
    mistake and ask again until the chances are gone.
    If the answer is correct, the function prints the phrases again, but with the gap
    filled in and goes to the next blank and so on.
    Args:
        chances (int): a critério do usuário.
        phrasess (string)
        gaps (list)
        answers (list)
    Returns:
        (string) "lose", "win"
    """
    remaining_chances = chances
    for index, gap in enumerate(gaps):
        print ("\nThe phrases is: " + phrases)
        user_answer = input("Enter the answer to the gap" + gap + " : ")
        while user_answer != answers[index]:
            remaining_chances -= 1
            if remaining_chances > last_chance:
                user_answer = input("\nNot exactly, you still have " + str(remaining_chances) +
                                             " chances. Try again the answer to the gap: " + gap + " : ")
            if remaining_chances == last_chance:
                user_answer = input("\nNot exactly, this is the last chance. Try one more time the answer to the gap: " + gap + " : ")
            if remaining_chances < last_chance:
                return "lose"
                break
        print ("\nWell done!\n")
        phrases = phrases.replace(gaps[index], user_answer)
    return "win"

def final_message(result):
    """
    Shows a win or lose message
    Args:
        result(string): "You lose", "You win"
    Returns:
        (string)"CONGRATULATIONS!!! YOU'VE FINISHED THE GAME!!!", "WHAT A PITY!!! THE CHANCES ARE OVER. ARE WE TRYING AGAIN?"
    """
    if result == "win":
            print ("\nCONGRATULATIONS!!! YOU FINISHED THE GAME!!!\n")
    if result == "lose":
        print ("\nWHAT A PITY!!! THE CHANCES ARE OVER. ARE WE TRYING AGAIN?\n")


def start_game():
    """
    game skeleton
    """
    presentation()
    level = select_level()
    chances = select_number_of_chances()
    phrases, gaps, answers = load_phrases_gaps_response(level)
    result = play(chances, phrases, gaps, answers)
    final_message(result)


start_game()
