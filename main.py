import random


def validate_pos_num(num):
    try:
        parsed = int(num)
    except ValueError:
        raise ValueError('Input must be an integer')

    if parsed < 0:
        raise ValueError('Input must be non-negative')

    return parsed


def get_positive_int(prompt):
    while True:
        num = input(prompt)
        try:
            return validate_pos_num(num)
        except ValueError as e:
            print(e)


def validate_range(min_value: int, max_value: int):
    if min_value > max_value:
        temp = max_value
        max_value = min_value
        min_value = temp
    return min_value, max_value


def get_range():
    min_value = get_positive_int('Enter minimal value: >>> ')
    max_value = get_positive_int('Enter maximum value: >>> ')

    return validate_range(min_value, max_value)


def check_input(random_num: int, user_num: int):
    if user_num > random_num:
        msg = 'Enter smaller number'
        return False, msg
    elif user_num < random_num:
        msg = 'Enter bigger number'
        return False, msg
    else:
        msg = 'You guessed correctly'
        return True, msg


def game_loop():
    results = []
    msg = 'default'
    check = False

    min_value, max_value = get_range()

    print(min_value, max_value)
    random_num = random.randint(min_value, max_value)
    while not check:
        user_num = get_positive_int(f'Try to guess number between {min_value} and {max_value}: >> ')
        if user_num in range(min_value, max_value + 1):
            check, msg = check_input(random_num, user_num)
            print(msg)
            results.append(msg)
        else:
            print(f'Enter value in given range({min_value}, {max_value})')
    return results


def main():
    game_info = game_loop()
    print(game_info)


if __name__ == '__main__':
    main()
