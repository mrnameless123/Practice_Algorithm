def number_needed(a, b):
    #map to hash table
    dictionary_a = {}
    number_of_delete = 0
    for x in a:
        if dictionary_a.get(x):
            dictionary_a[x] +=1
        else:
            dictionary_a[x] = 1
    for x in b:
        if dictionary_a.get(x):
            dictionary_a[x] -= 1
        else:
            number_of_delete += 1
    for key, value in dictionary_a.items():
        if value != 0:
            number_of_delete += 1
    return number_of_delete

a = input().strip()
b = input().strip()

print(number_needed(a, b))