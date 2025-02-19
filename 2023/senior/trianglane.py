columns = int(input())
row_one = [int(num) for num in input().split()]
row_two = [int(num) for num in input().split()]
perimeter = 3*(row_one.count(1) + row_two.count(1))

for i in range(columns):
    if (i+1) < columns:
        if row_one[i] == 1 and row_one[i+1] == 1:
            perimeter -= 2
        if row_two[i] == 1 and row_two[i+1] == 1:
            perimeter -= 2
    if row_one[i] == 1 and row_two[i] == 1:
        if i % 2 == 0:
            perimeter -= 2

print(perimeter)