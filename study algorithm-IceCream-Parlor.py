def get_key(a):
    return a[1]


def get_cost(a):
    return a[0]


def binary_search(list_cream, total_money):
    for index, x in enumerate(list_cream):
        residual = total_money - get_cost(x)
        if residual > 0:
            first = index + 1
            last = len(list_cream) - 1
            while first <= last:
                middle = (first + last) // 2
                if get_cost(list_cream[middle]) == residual:
                    return sorted([get_key(list_cream[middle]), get_key(x)])
                else:
                    if residual < get_cost(list_cream[middle]):
                        last = middle
                    else:
                        first = middle


def hash_search(flavors, money):
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
    return hash_search(ice_cream, total_money)
    # return binary_search(ice_cream, total_money)


T = int(input().strip())
for a in range(T):
    total_money = int(input().strip())
    no_id = int(input().strip())
    costs = list(map(int, input().strip().split(' ')))

    result_arr = solve(total_money, costs)
    print(result_arr[0], result_arr[1])