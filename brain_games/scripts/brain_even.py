from random import randint

import prompt


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def main_logic():

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name ? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 1

    while counter <= 3:
        random_number = randint(0, 100)
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        result = is_even(random_number)
        if answer == "no" and not result:
            print("Correct!")
            counter = counter + 1
        elif answer == "yes" and result:
            print("Correct!")
            counter = counter + 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            break
        
    print(f"Congratulations, {name}!")


def main():
    main_logic()


if __name__ == "__main__":
    main()



        
