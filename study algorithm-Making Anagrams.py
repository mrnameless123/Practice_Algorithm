def number_needed(a, b):
    table_freq = {}
    number_concat = 0
    for x in a:
        if table_freq.get(x):
            table_freq[x] += 1
        else:
            table_freq[x] = 1
    for x in b:
        if table_freq.get(x):
            table_freq[x] -= 1
        else:
            number_concat += 1
    for key, value in table_freq.items():
        if value != 0:
            number_concat += abs(value)
    return number_concat

a = input().strip()
b = input().strip()

print(number_needed(a, b))