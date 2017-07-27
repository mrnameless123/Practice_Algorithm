# import sys
#
# def solve(param_list1, param_list2, param_list3):
#     if sum(param_list1) == sum(param_list2) == sum(param_list3):
#         return sum(param_list1)
#
#     max_of_all = max(sum(param_list1), sum(param_list2), sum(param_list3))
#     if sum(param_list1) == max_of_all:
#         param_list1.pop()
#     elif sum(param_list2) == max_of_all:
#         param_list2.pop()
#     else:
#         param_list3.pop()
#     return solve(param_list1, param_list2, param_list3)
#
#
# n1, n2, n3 = input().strip().split(' ')
# n1, n2, n3 = [int(n1), int(n2), int(n3)]
# h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
# h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
# h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
# print(solve(h1, h2, h3))


#TODO: Better solution
# !/bin/python3

import sys


def alter_list(param_list1):
    out = []
    value = 0
    for x in range(len(param_list1) - 1, -1, -1):
        value += param_list1[x]
        out.append(value)
    out.insert(0, 0)
    return out


def solve(param_list1, param_list2, param_list3):
    alter1 = alter_list(param_list1)
    alter2 = alter_list(param_list2)
    alter3 = alter_list(param_list3)

    top1 = alter1.pop()
    top2 = alter2.pop()
    top3 = alter3.pop()
    while True:
        if top1 == top2:
            if top1 == top3:
                return top1
        if top1 == max(top1, top2, top3):
            top1 = alter1.pop()
        elif top2 == max(top1, top2, top3):
            top2 = alter2.pop()
        else:
            top3 = alter3.pop()



n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
print(solve(h1, h2, h3))
