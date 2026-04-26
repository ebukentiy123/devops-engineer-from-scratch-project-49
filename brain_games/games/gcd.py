from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def get_round_data():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(find_gcd(number1, number2))
    return question, correct_answer