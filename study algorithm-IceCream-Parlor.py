def get_key(a):
    return a[1]
def get_cost(a):
    return a[0]

def binary_search(start, end, a, search):
    first = start
    last = end
    while first <= last:
        middle = int(first + (last-first)/2)
        if get_cost(a[middle]) == search:
            return middle
        if get_cost(a[middle]) < search:
            first = middle
        else:
            last = middle
    return -1


def search(flavors, money):
    flavor_map = {}
    for element in flavors:
        flavor, index = element
        residual = money - flavor
        if residual > 0:
            if residual in flavor_map:
                return sorted([index, flavor_map[residual]])
            if not flavor in flavor_map:
                flavor_map[flavor] = index


def solve(total_money, list_cost):
    list_id = [x for x in range(1, len(list_cost) + 1)]
    ice_cream = tuple(zip(list_cost, list_id))
    ice_cream = sorted(ice_cream, key=get_cost)
    return search(ice_cream, total_money)


T = int(input().strip())
for a in range(T):
    total_money = int(input().strip())
    no_id = int(input().strip())
    costs = list(map(int, input().strip().split(' ')))

    result_arr = solve(total_money, costs)
    print(result_arr[0] + 1, result_arr[1] + 1)

