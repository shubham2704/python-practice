# W = 41
# val = [57 ,95 ,13 ,29, 1 ,99, 34, 77, 61 ,23, 24 ,70 ,73 ,88 ,33, 61 ,43 ,5 ,41 ,63 ,8 ,67, 20, 72, 98, 59, 46, 58 ,64, 94, 97, 70, 46, 81, 42 ,7 ,1 ,52 ,20 ,54 ,81, 3 ,73 ,78 ,81, 11, 41, 45, 18, 94, 24, 82 ,9 ,19, 59, 48 ,2, 72]
# wt= [83, 84, 85, 76 ,13 ,87, 2, 23, 33 ,82 ,79, 100 ,88 ,85 ,91, 78, 83 ,44 ,4 ,50 ,11, 68 ,90 ,88, 73, 83, 46 ,16, 7, 35, 76, 31, 40 ,49, 65 ,2, 18 ,47, 55, 38 ,75 ,58, 86, 77, 96, 94, 82, 92, 10 ,86, 54 ,49 ,65, 44, 77, 22 ,81 ,52]
# n = len(val)

# t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

# def knapSack(W, wt, val, n):
#     if n == 0 or W == 0:
#         return 0
#     if t[n][W] != -1:
#         return t[n][W]

#     if wt[n - 1] <= W:
#         t[n][W] = max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), knapSack(W, wt, val, n - 1))
#         return t[n][W]


#     elif wt[n-1] > W:
#         t[n][W] = knapSack(W, wt, val, n - 1)
#         return t[n][W]


# print(knapSack(W,wt,val,n))


import itertools as it
from itertools import combinations

s = list(range(5))
W = list(it.chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))
wh = 41

def knapsack_01_brute_combinatorial(values, weights, weight):
    from itertools import chain, combinations
    from functools import reduce
    s = zip(values, weights)
    combos = chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))
    result = filter(lambda x: x[1] <= weight,
                    map(lambda z: reduce(lambda a, y: (a[0] + y[0], a[1] + y[1]),
                                         z), combos))

    result = max(result, key=lambda x: x[0])[0]
    return result

print(knapsack_01_brute_combinatorial(s,W,wh))