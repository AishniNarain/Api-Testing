from mocking.dice import roll_dice

def guess_number(number):
    result = roll_dice()
    if result == number:
        return "You Won!"
    else:
        return "You lost!"

