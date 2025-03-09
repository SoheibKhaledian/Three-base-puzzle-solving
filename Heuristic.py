def heuristic(node, goal):
    return cost(node) + max(manhattan_distance(node.state, goal), stock_box(node.state, goal))


def tp_heuristic(node, goal):
    return max(manhattan_distance(node.state, goal) + distance_to_box(node.state, goal), stock_box(node.state, goal))


def cost(node):
    c = 0
    while node.depth > 0:
        c += 1
        if node.father_move in ['PU', 'PD', 'PR', 'PL']:
            c += 1
        node = node.father
    return c


def manhattan_distance(state, goal):
    min_h = float('inf')
    for B in state.bp:
        for G in goal:
            if B not in goal:
                h = abs(B[0] - G[0]) + abs(B[1] - G[1])
                if h < min_h:
                    min_h = h
    return min_h


def distance_to_box(state, goal):
    min_h = float('inf')
    for B in state.bp:
        if B not in goal:
            h = abs(B[0] - state.sx) + abs(B[1] - state.sy)
            if h < min_h:
                min_h = h
        return min_h


def stock_box(state, goal):
    element = ['S', '.', '@']
    for B in state.bp:
        stock = False
        if state.Map[B[0]][B[1] + 1] not in element and state.Map[B[0]][B[1] - 1] not in element:
            if B not in goal:
                stock = True
        else:
            continue

        if state.Map[B[0] + 1][B[1]] not in element and state.Map[B[0] - 1][B[1]] not in element:
            if B not in goal:
                stock = True
        else:
            stock = False

        if stock is True:
            return float('inf')

    return 0
