n = int(input())
array_a = [int(num) for num in input().split()]
array_b = [int(num) for num in input().split()]
repeated_nums = {}
repeated_nums_index_difference = {}
index = 0 
index_difference = 0

for num in array_b:
    if (num in array_b[(index + 1):]) or  (num in array_b[:index]):
    # if (index != 0 and  index != n-1) and (array_b[index] == array_b[index - 1] or array_b[index] == array_b[index + 1]):
    
        if repeated_nums.get(num) != None:
            repeated_nums[num].append(index)
        else: 
            repeated_nums[num] = [index]
    index += 1

for num in repeated_nums:
            first_index = repeated_nums[num][0]
            last_index = repeated_nums[num][-1]
            index_difference = last_index - first_index
            repeated_nums_index_difference[num] = index_difference
print(min(repeated_nums_index_difference.values()))
def swipe():
    answer = ""
    number_of_swipes = 0
    test_array = []
    

    if array_a == array_b:
        answer = "YES"
    else:
        for num, indicies in repeated_nums_index_difference:
            key = 0
            value = 0
            if num >= key and repeated_nums_index_difference[num] >= value:
                key = num
                value = repeated_nums_index_difference[num]
            test_array = []
            if test_array == array_b:
                pass
            print(min(repeated_nums_index_difference.values()))
        pass
    return answer, number_of_swipes
    
    
for num, indicies in repeated_nums_index_difference:
            key = 0
            value = 0
            if num >= key and repeated_nums_index_difference[num] >= value:
                key = num
                value = repeated_nums_index_difference[num]
print(key, value)

print(repeated_nums)
print(repeated_nums_index_difference)