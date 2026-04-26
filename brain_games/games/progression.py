from random import randint

DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_MIN_LENGTH = 5
PROGRESSION_MAX_LENGTH = 10


def generate_progression(start: int, step: int, length: int):
    return [start + i * step for i in range(length)]


def get_round_data():
    start = randint(1, 20)
    step = randint(1, 10)
    length = randint(PROGRESSION_MIN_LENGTH, PROGRESSION_MAX_LENGTH)

    progression = generate_progression(start, step, length)
    hidden_index = randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, correct_answer