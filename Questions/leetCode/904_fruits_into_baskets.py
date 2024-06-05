"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
"""
from collections import defaultdict
def totalFruits(fruits):
    # fruits [1, 2, 1] or [0, 1, 2, 2]
    # single row, from left to right, represented by integers, or the integer is the type of the fruit
    # so here [1, 2, 1] we have 2 fruits(1 and 2), and here we have 3 [0, 1, 2, 2](0, 1 and 2)

    # collect as much as possible
    # rules
    # only 2 baskets, each basket only single type of fruits
    # no limit on each basket
    # starting from any index, you must pick exactly on fruit from every tree while moving to the right
    count = defaultdict(int)
    l, total, res = 0, 0, 0

    for r in range(len(fruits)):
        count[fruits[r]] += 1 # this works because of the default dicts that initializes with0
        total += 1

        while len(count) > 2:
            f = fruits[l]
            count[f] -= 1
            total -= 1
            l += 1

            if not count[f]:
                count.pop(f)

        res = max(res, total)

    return res


if __name__ == "__main__":
    fruits =  [0, 1, 2, 2]
    print(totalFruits(fruits))