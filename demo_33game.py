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


def set_value(state, idx, who):
    # copy current state and set state[idx] as who
    # return the copy
    newstate = state.copy()
    newstate[idx] = who
    return newstate


continues = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # lines
             [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
             [0, 4, 8], [2, 4, 6]]  # cross


def check_if_threelink(state, who, continues=continues):
    # return True if there are three nodes linked
    return any((sum(state[_] for _ in c)) == 3*who for c in continues)


result_dict = dict()


def check_state(state, who):
    # pnt_board(state)

    if check_if_threelink(state, who):
        return True

    if any(check_if_threelink(p, -who) for p in possibles(state, -who)):
        return False

    if possibles(state, -who) == []:
        return False

    ll = list(any(check_state(p1, who) for p1 in possibles(p0, who))
              for p0 in possibles(state, -who))
    result_dict[str(state)] = ll
    # print(ll)
    if False in ll:
        return False
    return True


state = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

for p in possibles(state, 1):
    check_state(p, 1)

for p in possibles(state, 1):
    res = result_dict[str(p)]
    print(p, res, sum(res))


class Game_3x3:
    def __init__(self):
        self.shape = {0: ' ', 1: 'x', -1: 'o'}
        self.refresh()

    def refresh(self):
        self.state = list(0 for _ in range(9))
        self.who = 1

    def go(self):
        self.refresh()
        while True:
            pnt_board(self.state)
            idx = -1
            while idx not in range(9):
                idx = int(input(self.shape[self.who]+': '))
            self.state[idx] = self.who
            self.who *= -1


g3 = Game_3x3()
g3.go()
