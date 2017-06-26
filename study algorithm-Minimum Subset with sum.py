"""
Given an array and a number, create an algorithm that return a subset array of the given array
where: sum of the elements inside the subset array is greater than a number,
 the sum of element inside the subset array,as least elements as possible
is minimum
"""
def solve(param_sum, param_array):
    sorted_array = sorted(param_array, reverse=True)
    bigger_list = [i for i in sorted_array if (i-param_sum) >= 0]
    if len(bigger_list) > 0:
        return [min(bigger_list)]
    else:
        output = []
        index = 0
        residual = param_sum - sorted_array[index]
        while residual > 0:
            output.append(sorted_array[index])
            index +=1
            residual -=sorted_array[index]
        output.append(sorted_array[index])
        return output


sum = int(input().strip())
a = list(map(int, input().strip().split(' ')))

print(*solve(sum, a), sep=' ')


