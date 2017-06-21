import sys


size_A = int(input().strip())
list_A = list(map(int, input().strip().split(' ')))
size_B = int(input().strip())
list_B = list(map(int, input().strip().split(' ')))
#Check the list_B to make a hash table
hash_table = {}
for x in list_B:
    if hash_table.get(x) is None:
        hash_table[x] = 1
    else:
        hash_table[x] += 1
for x in list_A:
    hash_table[x] -= 1
for key, value in hash_table.items():
    if value != 0:
        print(key)
