import sys
def solve(param_input):
    open_bracket_stack = []
    for x in range(len(param_input)):
        if param_input[x] == '{' or param_input[x] == '(' or param_input[x] == '[':
            open_bracket_stack.append(param_input[x])
        else:
            if len(open_bracket_stack) > 0:
                top_open = open_bracket_stack.pop()
                current_bracket = param_input[x]
                if top_open == '{' and current_bracket != '}':
                    return 'NO'
                elif top_open == '[' and current_bracket != ']':
                    return 'NO'
                elif top_open == '(' and current_bracket != ')':
                    return 'NO'
            else:
                return 'NO'
    if len(open_bracket_stack) != 0:
        return 'NO'
    else:
        return 'YES'

# t = int(input().strip())
# for a0 in range(t):
#     s = input().strip()
#     print(solve(s))

#
t = int(input().strip())
list_output = []
actual = []
for a0 in range(t):
    s = input().strip()
    list_output.append(solve(s))
    # print(solve(s))
print('Oki now insert answer')
for _ in range(t):
    actual.append(input().strip())

for x in range(len(actual)):
    if actual[x] != list_output[x]:
        print('Error in case ', x)
        print('actual is {0} vs answer is {1}'.format(actual[x], list_output[x]))
