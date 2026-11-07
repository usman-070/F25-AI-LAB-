import math


def minimax(cur_depth, node_index, max_turn, scores, target_depth, count):
    if cur_depth == target_depth:
        count[0] = count[0] + 1
        return scores[node_index]
    if max_turn:
        return max(
            minimax(cur_depth + 1, node_index * 2, False, scores, target_depth, count),
            minimax(cur_depth + 1, node_index * 2 + 1, False, scores, target_depth, count),
        )
    return min(
        minimax(cur_depth + 1, node_index * 2, True, scores, target_depth, count),
        minimax(cur_depth + 1, node_index * 2 + 1, True, scores, target_depth, count),
    )


def alphabeta(depth, index, max_turn, scores, target, alpha, beta, count):
    if depth == target:
        count[0] = count[0] + 1
        return scores[index]
    if max_turn:
        value = float("-inf")
        for i in range(2):
            value = max(value, alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta, count))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    value = float("inf")
    for i in range(2):
        value = min(value, alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta, count))
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value


def run_both(scores, depth, label):
    count_min = [0]
    count_ab = [0]
    value_min = minimax(0, 0, True, scores, depth, count_min)
    value_ab = alphabeta(0, 0, True, scores, depth, float("-inf"), float("inf"), count_ab)
    print(label)
    print("Minimax value:", value_min, "| Leaves evaluated:", count_min[0])
    print("Alpha-beta value:", value_ab, "| Leaves evaluated:", count_ab[0])
    print("Same result:", value_min == value_ab)


scores1 = [3, 5, 2, 9, 0, 7]
depth1 = math.ceil(math.log2(len(scores1)))
scores1 = scores1 + [0] * (2**depth1 - len(scores1))
run_both(scores1, depth1, "Tree 1 (manual Minimax tree, padded):")

scores2 = [3, 5, 2, 9, 3, 5, 2, 9]
depth2 = int(math.log2(len(scores2)))
run_both(scores2, depth2, "Tree 2 (manual alpha-beta tree):")

scores3 = [2, 9, 3, 5, 2, 9, 3, 5]
run_both(scores3, depth2, "Tree 2 reordered (worst order):")

count_min = [0]
count_ab = [0]
print("Edge case, single leaf [7]:")
print("Minimax value:", minimax(0, 0, True, [7], 0, count_min), "| Leaves evaluated:", count_min[0])
print("Alpha-beta value:", alphabeta(0, 0, True, [7], 0, float("-inf"), float("inf"), count_ab), "| Leaves evaluated:", count_ab[0])
