# code: utf-8

shape = {0: ' ', 1: 'x', -1: 'o'}


def pnt_board(state, shape=shape):
    # print board as input state
    print('_' * 7, end='')
    for j, s in enumerate(state):
        if j % 3 == 0:
            print('\n', end='|')
        if s == 0:
            print(j, end='|')
        else:
            print(shape[s], end='|')
    print('')
    print('-' * 10)


def possibles(state, nxt):
    # list all possible states
    # nxt: 1 or -1 for next input
    # return all possible next state
    idx = list(_ for _ in range(9) if state[_] == 0)
    possibles_list = list(set_value(state, i, nxt) for i in idx)
    return possibles_list


def set_value(state, idx, nxt):
    # copy current state and set state[idx] as nxt
    # return the copy
    newstate = state.copy()
    newstate[idx] = nxt
    return newstate


continues = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # lines
             [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
             [0, 4, 8], [2, 4, 6]]  # cross


def check_if_win(state, continues=continues):
    # return True if there are three nodes linked
    return any(abs(sum(state[_] for _ in c)) == 3 for c in continues)


state = [1, 1, 0,
         0, 1, 0,
         0, 0, 0]

pnt_board(state)

poss = possibles(state, -1)
for p in poss:
    pnt_board(p)
    print(check_if_win(p))
