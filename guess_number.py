"""It's the game "Guess number."""

from random import randint

SECRET_NUMBER = randint(0, 100)


def main():
    """The game itself."""
    print("Welcome to the \"Guess number\" game.")
    playing = True

    while playing:
        answer = input("Enter the integer number between 0 and 100 or type "
                       "exit to quit the game: ").lower()

        if answer == "exit":
            print("Good luck! The secret number was", SECRET_NUMBER)
            break

        try:
            answer = valid_answer(answer)
        except ValueError:
            print("The answer must be integer number between 0 and 100!")
            continue

        playing = right_answer(answer)


def right_answer(answer):
    """
    Compares player's answer with the secret number.

    :param answer: Player's answer.
    :type answer: int

    :return: True of False
    :rtype: bool
    """
    global SECRET_NUMBER

    if answer < SECRET_NUMBER:
        print(f"Your answer ({answer}) is lower than secret number.")
    elif answer > SECRET_NUMBER:
        print(f"Your answer ({answer}) is higher than secret number.")
    else:
        print("You won! Do you want to play another game?", end=" ")

        if input("Enter yes to continue: ").lower() == "yes":
            SECRET_NUMBER = randint(0, 100)
        else:
            print("Good luck!")
            return False

    return True


def valid_answer(answer):
    """
    Checks if an answer is valid.

    :param answer: Player's answer.
    :type answer: str

    :raise ValueError if answer is not a number between 0 and 100.

    :return: Player's answer.
    :rtype: int
    """
    answer = int(answer)
    if not 0 <= answer <= 100:
        raise ValueError
    return answer


if __name__ == "__main__":
    main()
