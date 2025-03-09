m = [1, 0, 89, 90, 67, 34, 9, 8, 2, 90, 65, 23, 34]

if __name__ == '__main__':
    print(sorted(m))


# def moves(dad: Node):
#     # if dad.depth > 10:
#     #     return []
#
#     possible_moves = list()
#     if dad.state.Map[dad.state.sx + 1][dad.state.sy] != '#' and dad.state.Map[dad.state.sx + 1][dad.state.sy] != '@':
#         ns = copy.deepcopy(dad.state)
#
#         ns.Map[ns.sx][ns.sy] = '.'
#         ns.Map[ns.sx + 1][ns.sy] = 'S'
#
#         ns.sx += 1
#
#         possible_moves .append(Node(ns, dad, 'D', dad.depth+1))
#     elif dad.state.Map[dad.state.sx + 1][dad.state.sy] == '@' and dad.state.Map[dad.state.sx + 2][dad.state.sy] != '#':
#         ns = copy.deepcopy(dad.state)
#
#         ns.Map[ns.sx][ns.sy] = '.'
#         ns.Map[ns.sx + 1][ns.sy] = 'S'
#         ns.Map[ns.sx + 1][ns.sy] = '@'
#
#         ns.bp.remove([ns.sx + 1, ns.sy])
#         ns.bp.append([ns.sx + 2, ns.sy])
#
#         ns.sx += 1
#
#         possible_moves .append(Node(ns, dad, 'PD', dad.depth+1))
#
#     if dad.state.Map[dad.state.sx - 1][dad.state.sy] != '#' and dad.state.Map[dad.state.sx - 1][dad.state.sy] != '@':
#         ns = copy.deepcopy(dad.state)
#
#         ns.Map[ns.sx][ns.sy] = '.'
#         ns.Map[ns.sx - 1][ns.sy] = 'S'
#
#         ns.sx -= 1
#
#         possible_moves .append(Node(ns, dad, 'U', dad.depth+1))
#     elif dad.state.Map[dad.state.sx - 1][dad.state.sy] == '@' and dad.state.Map[dad.state.sx - 2][dad.state.sy] != '#':
#         ns = copy.deepcopy(dad.state)
#
#         ns.Map[ns.sx][ns.sy] = '.'
#         ns.Map[ns.sx - 1][ns.sy] = 'S'
#         ns.Map[ns.sx - 2][ns.sy] = '@'
#
#         ns.bp.remove([ns.sx - 1, ns.sy])
#         ns.bp.append([ns.sx - 2, ns.sy])
#
#         ns.sx -= 1
#
#         possible_moves .append(Node(ns, dad, 'PU', dad.depth+1))
#
#     if dad.state.Map[dad.state.sx][dad.state.sy + 1] != '#' and dad.state.Map[dad.state.sx][dad.state.sy + 1] != '@':
#         ns = copy.deepcopy(dad.state)
#
#         ns.Map[ns.sx][ns.sy] = '.'
#         ns.Map[ns.sx][ns.sy + 1] = 'S'
#
#         ns.sy += 1
#
#         possible_moves .append(Node(ns, dad, 'R', dad.depth+1))
#     elif dad.state.Map[dad.state.sx][dad.state.sy + 1] == '@' and dad.state.Map[dad.state.sx][dad.state.sy + 2] != '#':
#         ns = copy.deepcopy(dad.state)
#
#         ns.Map[ns.sx][ns.sy] = '.'
#         ns.Map[ns.sx][ns.sy + 1] = 'S'
#         ns.Map[ns.sx][ns.sy + 2] = '@'
#
#         ns.bp.remove([ns.sx, ns.sy + 1])
#         ns.bp.append([ns.sx, ns.sy + 2])
#
#         ns.sy += 1
#
#         possible_moves .append(Node(ns, dad, 'PR', dad.depth+1))
#
#     if dad.state.Map[dad.state.sx][dad.state.sy - 1] != '#' and dad.state.Map[dad.state.sx][dad.state.sy - 1] != '@':
#         ns = copy.deepcopy(dad.state)
#
#         ns.Map[ns.sx][ns.sy] = '.'
#         ns.Map[ns.sx][ns.sy - 1] = 'S'
#
#         ns.sy -= 1
#
#         possible_moves .append(Node(ns, dad, 'L', dad.depth+1))
#     elif dad.state.Map[dad.state.sx][dad.state.sy - 1] == '@' and dad.state.Map[dad.state.sx][dad.state.sy - 2] != '#':
#         ns = copy.deepcopy(dad.state)
#
#         ns.Map[ns.sx][ns.sy] = '.'
#         ns.Map[ns.sx][ns.sy - 1] = 'S'
#         ns.Map[ns.sx][ns.sy - 2] = '@'
#
#         ns.bp.remove([ns.sx, ns.sy - 1])
#         ns.bp.append([ns.sx, ns.sy - 2])
#
#         ns.sy += 1
#
#         possible_moves .append(Node(ns, dad, 'PL', dad.depth+1))
#
#     return possible_moves
# def dfs(nodes, goal, i=1, ni=1):
#     try:
#         if not nodes:
#             print('no way found')
#             return None
#
#         node = nodes.pop()
#         if condition_check(node.state.bp, goal):
#             path(node, i, ni)
#             return None
#
#         node.children = moves(node)
#         nodes += node.children
#
#         i += 1
#         ni += len(node.children)
#
#         # print(node.state.sx, node.state.sy, node.state.bp)
#         return dfs(nodes, goal, i, ni)
#     except RecursionError:
#         print(f'there was loop\nnumber of node checked {i}\nnumber of node created {ni}')
# def a_star(nodes, goal, i=1, ni=1):
#     if not nodes:
#         print('no way found')
#         return None
#
#     for node in nodes:
#         if node.heuristic is None:
#             node.heuristic = heuristic(node, goal)
#
#     nodes = sorted(nodes, key=lambda x: x.heuristic)
#
#     node = nodes[0]
#
#     if node.heuristic == float('inf'):
#         print('\n')
#         print(node.state.bp)
#         for l in node.state.Map:
#             for d in l:
#                 print(d, end='')
#
#         print('\n')
#         return None
#
#     if condition_check(node.state.bp, goal):
#         path(node, i, ni)
#         return None
#
#     node.children = moves(node)
#     i += 1
#     ni += len(node.children)
#
#     a_star(nodes[1:] + node.children, goal, i, ni)
# def manhattan_distance(state, goal):
#     min_h = float('inf')
#     for B in state.bp:
#         for G in goal:
#             if B not in goal:
#                 h = abs(B[0] - G[0]) + abs(B[1] - G[1])
#                 if h < min_h:
#                     min_h = h
#     return min_h
# def manhattan_distance(state, goal):
#     total_distance = 0
#     for B in state.bp:
#         min_h = float('inf')
#         for G in goal:
#             h = abs(B[0] - G[0]) + abs(B[1] - G[1])
#             if h < min_h:
#                 min_h = h
#         total_distance += min_h
#     return total_distance