def solution(numbers, target):
    tree = [0]
    for i in numbers:
        sub_tree = []
        for j in tree:
            sub_tree.append(j + i)
            sub_tree.append(j - i)
        tree = sub_tree

    return tree.count(target)
