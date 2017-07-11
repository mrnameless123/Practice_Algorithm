
N = int(input().strip())
list_N = [input().strip() for _ in range(N)]
Q = int(input().strip())
list_Q = [input().strip() for _ in range(Q)]
dict_Q = {}
for x in list_Q:
    dict_Q[x] = 0

for x in list_N:
    if dict_Q.get(x) is not None:
        dict_Q[x] += 1


for x in list_Q:
    print(dict_Q[x])