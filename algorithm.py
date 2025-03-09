from Def import *
from Heuristic import heuristic, tp_heuristic


def condition_check(boxes, goal):
    for b in boxes:
        if b not in goal:
            return False
    return True


def dfs(nodes, goal):
    i = 0
    ni = 1

    while nodes:
        node = nodes.pop()

        # if is_loop(node):
        #     print('there is loop')
        #     return None

        if condition_check(node.state.bp, goal):
            path(node, i, ni)
            return node

        node.children = moves(node)

        for child in node.children:
            exist = False
            dad = node.father
            while dad is not None:
                if child.state.Map == dad.state.Map:
                    exist = True
                    break
                dad = dad.father
            if exist is False:
                nodes.append(child)

        ni += len(node.children)

        i += 1

    print(f'no way found: {i}, {ni}')
    return None


def bfs(nodes, goal):
    closed = set()
    i = 0
    ni = 1

    while nodes:
        node = nodes[0]
        nodes = nodes[1:]

        # print('\n')
        # for l in node.state.Map:
        #     for h in l:
        #         print(h, end='')
        #
        # print('\n')

        if condition_check(node.state.bp, goal):
            path(node, i, ni)
            return node

        closed.add(tuple(map(tuple, node.state.Map)))

        node.children = moves(node)

        for child in node.children:
            child_map_tuple = tuple(map(tuple, child.state.Map))
            if child_map_tuple not in closed:
                nodes.append(child)
                ni += 1

        i += 1

    print(f'no way found: {i}, {ni}')
    return None


def a_star(nodes, goal):
    i = 0
    ni = 1

    while nodes:
        for node in nodes:
            if node.heuristic is None:
                node.heuristic = heuristic(node, goal)

        nodes = sorted(nodes, key=lambda x: x.heuristic)

        node = nodes[0]
        nodes = nodes[1:]

        if node.heuristic == float('inf'):
            print('\n')
            print(node.state.bp)
            for l in node.state.Map:
                for d in l:
                    print(d, end='')

            print('\n')
            return None

        if condition_check(node.state.bp, goal):
            path(node, i, ni)
            return None

        node.children = moves(node)
        i += 1
        ni += len(node.children)

        nodes += node.children

    print(f'no way found: {i}, {ni}')
    return None


def tp(node, goal):
    ni = 1
    i = 1
    node.heuristic = tp_heuristic(node, goal)

    # print(node.heuristic)

    while node:
        if node.heuristic == float('inf'):
            print('\n')
            print(node.state.bp)
            for l in node.state.Map:
                for d in l:
                    print(d, end='')

            print('\n')
            return None

        if condition_check(node.state.bp, goal):
            path(node, i, ni)
            return None

        i += 1

        node.children = moves(node)
        for child in node.children:
            child.heuristic = tp_heuristic(child, goal)
            ni += 1
            # print(child.heuristic)

        if node.children is None:
            print(f'there is no more move {i} {ni}')
            return None

        sort_children = sorted(node.children, key=lambda x: x.heuristic)

        if sort_children[0].heuristic <= node.heuristic:
            node = sort_children[0]
        else:
            print(f'there is no more better move {i} {ni}')
            return None

    print(f'no way found: {i}, {ni}')
    return None
