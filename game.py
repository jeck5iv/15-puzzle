# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
import random
import sys

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This function is used to create a field at the very start of the game.

    :return: list with 16 randomly shuffled tiles,
        one of which is a empty space.
    """

    def field_gen():
        cells_mass = [(i + 1) for i in range(16)]
        cells_mass[-1] = EMPTY_MARK
        return cells_mass

    def shuffle(any_field):
        moves_list = list(MOVES.keys())
        for i in range(random.randint(1000, 2000)):
            next_move = random.choice(moves_list)
            perform_move(any_field, next_move, print_flag=False)
        return any_field

    return shuffle(field_gen())


def print_field(field):
    def print_string(start, length=4):
        for i in range(start, start + length):
            print('| ', end='')
            if len(str(field[i])) == 1:
                print(' ', end='')
            print(field[i], end='')
        print('|')

    horizontal_string = '—' * 17
    print(horizontal_string)
    for i in range(4):
        print_string(i * 4)
        print(horizontal_string)
    print()
    return


def is_game_finished(field):
    """
        This function checks if the game is finished.

        :param field: current field state.
        :return: True if the game is finished, False otherwise.
        """

    for i in range(len(field) - 1):
        if field[i] != i + 1:
            return False
    return True


def perform_move(field, key, print_flag=True):
    """
        Moves empty-tile inside the field.

        :param field: current field state.
        :param key: move direction.
        :param print_flag: at the end prints field if True
        :optional param print_flag (default = True): False if you dont want to print error messages and playfield.
        :return: new field state (after the move)
            or `None` if the move can't me done.
        """
    if key == '#':
        return

    x_index = field.index('x')
    next_x_index = x_index + MOVES[key]

    check_ws = key in {'w', 's'} and (next_x_index in range(16))
    check_ad = key in {'a', 'd'} and (x_index // 4 == next_x_index // 4)
    if not (check_ws or check_ad):
        if print_flag:
            print('Incorrect move. You are trying to go outside the boundary of the playing field.')
        return
    else:
        field[x_index], field[next_x_index] = field[next_x_index], field[x_index]
        if print_flag:
            print_field(field)
        return field


def handle_user_input():
    """
        Handles user input.

        List of accepted moves:
            'w' - up,
            's' - down,
            'a' - left,
            'd' - right

        :return: <str> current move.
    """

    key = input()
    if key not in MOVES.keys():
        print("Incorrect input. Please use only commands 'w', 's', 'a', or 'd'.")
        return '#'
    return key
    pass


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    field = shuffle_field()
    print_field(field)
    steps_count = 0

    print("I'am sure you know the rules. Use 'w', 's', 'a', or 'd' to move 'x'.")
    print()
    while not is_game_finished(field):
        try:
            print('Perform your next move: ', end='')
            key = handle_user_input()
            steps_count += perform_move(field, key) is not None
        except KeyboardInterrupt:
            print('\n\nLoser.')
            sys.exit()
    print('Congratulations! You won!. You solved this puzzle in', steps_count, 'steps. Not bad.')


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
