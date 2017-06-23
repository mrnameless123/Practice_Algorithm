import sys


def solve(a):
    left_index = 0
    right_index = len(a)-1
    left = a[left_index]
    right = a[right_index]
    while left_index != right_index:
        if left < right:
            left_index +=1
            left += a[left_index]
        else:
            right_index -= 1
            right += a[right_index]
    if left == right:
        return 'YES'
    return 'NO'


T = int(input().strip())
for q in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)