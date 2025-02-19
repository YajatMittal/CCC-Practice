n = int(input())
hat_nums = []
total = 0

for num in range(n):
    hat_nums.append(int(input()))

for i in range(n):
    if i >= (n/2):
        opposite = i - (n/2)
    else:
        opposite = i + (n/2)

    if hat_nums[i] == hat_nums[int(opposite)]:
        total += 1

print(total)
