# N = int(input().strip())
# list_element = []
# for x in range(N):
#     k = list(map(int, input().strip().split(' ')))
#     if k[0] == 1:
#         value  = k[1]
#         list_element.append(value)
#     elif k[0] == 2:
#         list_element.pop()
#     elif k[0] == 3:
#         print(max(list_element))

#TODO: The previous code is good but it take to long time to find the max element within the stack
'''
Alternating solution
'''
N = int(input().strip())
list_element = []
max_val = -1
for x in range(N):
    k = list(map(int, input().strip().split(' ')))
    if k[0] == 1:
        value  = k[1]
        max_val = max(max_val, value)
        list_element.append((value, max_val))
    elif k[0] == 2:
        if len(list_element) > 0:
            list_element.pop()
        if len(list_element) == 0:
            max_val = -1
        else:
            max_val = list_element[len(list_element)-1][1]
    elif k[0] == 3:
        if len(list_element) != 0:
            print(list_element[len(list_element)-1][1])