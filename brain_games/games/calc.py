from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def calculate(num_one: int, num_two: int, sign: str) -> int:
    if sign == "+":
        return num_one + num_two
    if sign == "-":
        return num_one - num_two
    if sign == "*":
        return num_one * num_two
    raise ValueError(f"Unknown sign: {sign}")


def get_round_data():
    signs = ["*", "+", "-"]
    sign = choice(signs)
    num_one = randint(0, 100)
    num_two = randint(0, 100)

    question = f"{num_one} {sign} {num_two}"
    result = calculate(num_one, num_two, sign)
    correct_answer = str(result)

    return question, correct_answer