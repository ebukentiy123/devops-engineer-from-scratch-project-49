from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_round_data():
    number = randint(0, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer