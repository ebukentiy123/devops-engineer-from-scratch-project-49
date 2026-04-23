from random import randint

import prompt

def expression(num_one, num_two, random_sign):
    match random_sign:
        case "+":
            return num_one + num_two
        case "-":
            return num_one - num_two
        case "*":
            return num_one * num_two
        



def main_logic():

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name ? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')

    counter = 0

    while counter <= 2:
        sign = ["*", "+", "-"]
        random_sign = sign[randint(0, 2)]

        random_number_one = randint(0, 100)
        random_number_two = randint(0, 100)

        result = expression(random_number_one, random_number_two, random_sign)
        print(f"Question: {random_number_one} {random_sign} {random_number_two}")
        answer = prompt.string("Your answer: ")

        if answer.isdigit():
            if int(answer) == result:
                print("Correct!")
                counter = counter + 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
                print(f"Let's try again, {name}!")
                break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break

    if counter == 3:
        print(f"Congratulations, {name}!")


def main():
    main_logic()


if __name__ == "__main__":
    main()