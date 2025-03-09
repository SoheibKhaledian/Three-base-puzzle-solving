from algorithm import *


def read_file(add):
    f = open(add, 'r')
    line = f.readline()
    row, column = line.split(' ')

    sx, sy = None, None
    bp = list()
    gp = list()

    Map = list()
    for x in range(int(row)):
        line = f.readline()
        L = list()

        for y, d in enumerate(line):
            if d == 'S':
                sx = x
                sy = y
            elif d == '@':
                bp.append([x, y])
            elif d == 'X':
                d = '.'
                gp.append([x, y])

            L.append(d)

        Map.append(L)

    return repository([Map, sx, sy, bp, gp])


class repository:
    def __init__(self, repository_data):
        self.Map, self.sx, self.sy, self.bp, self.gp = repository_data
        self.first_state = State(self.sx, self.sy, self.bp, self.Map)


class State:
    def __init__(self, sx, sy, bp, map):
        self.sx, self.sy = sx, sy
        self.bp = bp
        self.Map = map


if __name__ == '__main__':
    rep = read_file('Input.txt')

    for l in rep.first_state.Map:
        for i in l:
            print(i, end='')
    # print('\n')

    while 1:
        algorithms = input('name the algorithm(DFS, BFS, A, TP or E for exit) -> ').upper()

        if algorithms == 'E':
            break

        if 'DFS' in algorithms:
            dfs([Node(rep.first_state)], rep.gp)
        if 'BFS' in algorithms:
            bfs([Node(rep.first_state)], rep.gp)
        if 'A' in algorithms:
            a_star([Node(rep.first_state)], rep.gp)
        if 'TP' in algorithms:
            tp(Node(rep.first_state), rep.gp)

    # ns = State(1, 1, [[1, 3], [4, 6]], 1)
    # print(rep.first_state.sx, rep.first_state.sy)
    # print(condition_check(ns, [[1, 3], [4, 9]]))
    # print(rep.Map)
    # print(rep.bp, '\n', rep.gp)
