from argparse import ArgumentParser
import random

parser = ArgumentParser()

MIN_VALUE = 0
MAX_VALUE = 100

parser.add_argument('-g', '--guess', type=int, help='Enter number between given range ', )


def generate_number(min_range=0, max_range=100):
    rand_num = random.randint(min_range, max_range)
    return rand_num


def user_int(prompt):
    global user_num
    while True:
        try:
            user_num = int(input(prompt))
            break

        except ValueError:
            print('Enter correct value(int)')
    return user_num


def check_input(random_num: int, user_num: int):
    if user_num > random_num:
        print('Enter smaller number')
        return False
    elif user_num < random_num:
        print('Enter bigger number')
        return False
    else:
        print('You guessed correctly')
        return True


def main():
    check = False
    random_num = generate_number(MIN_VALUE, MAX_VALUE)
    while not check:
        user_num = user_int(f'Try to guess number between {MIN_VALUE} and {MAX_VALUE}: >> ')
        check = check_input(random_num, user_num)


if __name__ == '__main__':
    main()
