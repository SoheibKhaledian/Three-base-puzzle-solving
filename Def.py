import copy


class Node:
    def __init__(self, state, father=None, father_move=None, depth=0, heuristic=None):
        self.children = list()
        self.father = father
        self.father_move = father_move
        self.state = state
        self.depth = depth
        self.heuristic = heuristic


def moves(dad: Node):
    possible_moves = list()

    sx, sy = dad.state.sx, dad.state.sy
    Map = dad.state.Map
    bp = dad.state.bp

    # Move Down
    if Map[sx + 1][sy] != '#' and Map[sx + 1][sy] != '@':
        ns = copy.deepcopy(dad.state)
        ns.Map[sx][sy] = '.'
        ns.Map[sx + 1][sy] = 'S'
        ns.sx += 1
        possible_moves.append(Node(ns, dad, 'D', dad.depth + 1))
    elif Map[sx + 1][sy] == '@' and Map[sx + 2][sy] != '#':
        ns = copy.deepcopy(dad.state)
        ns.Map[sx][sy] = '.'
        ns.Map[sx + 1][sy] = 'S'
        ns.Map[sx + 2][sy] = '@'
        ns.bp.remove([sx + 1, sy])
        ns.bp.append([sx + 2, sy])
        ns.sx += 1
        possible_moves.append(Node(ns, dad, 'PD', dad.depth + 1))

    # Move Up
    if Map[sx - 1][sy] != '#' and Map[sx - 1][sy] != '@':
        ns = copy.deepcopy(dad.state)
        ns.Map[sx][sy] = '.'
        ns.Map[sx - 1][sy] = 'S'
        ns.sx -= 1
        possible_moves.append(Node(ns, dad, 'U', dad.depth + 1))
    elif Map[sx - 1][sy] == '@' and Map[sx - 2][sy] != '#':
        ns = copy.deepcopy(dad.state)
        ns.Map[sx][sy] = '.'
        ns.Map[sx - 1][sy] = 'S'
        ns.Map[sx - 2][sy] = '@'
        ns.bp.remove([sx - 1, sy])
        ns.bp.append([sx - 2, sy])
        ns.sx -= 1
        possible_moves.append(Node(ns, dad, 'PU', dad.depth + 1))

    # Move Right
    if Map[sx][sy + 1] != '#' and Map[sx][sy + 1] != '@':
        ns = copy.deepcopy(dad.state)
        ns.Map[sx][sy] = '.'
        ns.Map[sx][sy + 1] = 'S'
        ns.sy += 1
        possible_moves.append(Node(ns, dad, 'R', dad.depth + 1))
    elif Map[sx][sy + 1] == '@' and Map[sx][sy + 2] != '#':
        ns = copy.deepcopy(dad.state)
        ns.Map[sx][sy] = '.'
        ns.Map[sx][sy + 1] = 'S'
        ns.Map[sx][sy + 2] = '@'
        ns.bp.remove([sx, sy + 1])
        ns.bp.append([sx, sy + 2])
        ns.sy += 1
        possible_moves.append(Node(ns, dad, 'PR', dad.depth + 1))

    # Move Left
    if Map[sx][sy - 1] != '#' and Map[sx][sy - 1] != '@':
        ns = copy.deepcopy(dad.state)
        ns.Map[sx][sy] = '.'
        ns.Map[sx][sy - 1] = 'S'
        ns.sy -= 1
        possible_moves.append(Node(ns, dad, 'L', dad.depth + 1))
    elif Map[sx][sy - 1] == '@' and Map[sx][sy - 2] != '#':
        ns = copy.deepcopy(dad.state)
        ns.Map[sx][sy] = '.'
        ns.Map[sx][sy - 1] = 'S'
        ns.Map[sx][sy - 2] = '@'
        ns.bp.remove([sx, sy - 1])
        ns.bp.append([sx, sy - 2])
        ns.sy -= 1
        possible_moves.append(Node(ns, dad, 'PL', dad.depth + 1))

    return possible_moves


def path(node, i, ni):
    way = ''
    p = 0

    print(f'\nthe length of the path = {node.depth}\nnumber of checked node checked = {i}\nnumber of node created: {ni}')

    while node.depth > 0:
        way = node.father_move + ' ' + way
        if node.father_move in ['PU', 'PD', 'PR', 'PL']:
            p += 1
        node = node.father

    #     print('\n')
    #     for l in node.state.Map:
    #         for i in l:
    #             print(i, end='')
    #
    # print('\n')

    print(f"number of push = {p}\nway has found: {way}")


def is_loop(node):
    dad = node.father

    for i in range(12):
        if node is None or dad is None or dad.father is None:
            return False

        for l in node.state.Map:
            for i in l:
                print(i, end='')
        print('\n')

        if node.state.Map != dad.father.state.Map:
            return False
        else:
            node = dad
            dad = node.father

    return True
