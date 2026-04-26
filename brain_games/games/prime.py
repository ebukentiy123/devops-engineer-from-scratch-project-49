from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def get_round_data():
    number = randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer