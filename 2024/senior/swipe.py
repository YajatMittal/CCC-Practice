n = int(input())
array_a = [int(num) for num in input().split()]
array_b = [int(num) for num in input().split()]

if array_a == array_b:
    print("YES")
    print(0)
else:
    same =  []
    different = []
    if n == 2:
        for i in range(n):
            if array_a[i] != array_b[i]:
                different.append(array_a[i])
            else:
                same.append(array_a[i])
        for num in different:
            if different.index(num) == 0:
                print("YES")
                print(1)
                print(f"L {array_a[0]} {array_a[1]}")
            else:
                print("YES")
                print(1)
                print(f"R {array_a[0]} {array_a[1]}")
    else:
        if n% 2==0:
            print("NO")
        else:
            print("YES")

# same =  []
# different = []
# multiple = []
# for i in range(n):
#     if array_a[i] != array_b[i]:
#         different.append(array_a[i])
#     else:
#         same.append(array_a[i])

# for num in same:
#     count = array_b.count(num)
#     if count > 1:
#         multiple.append(num)
# l = same + 
# multiple.count()
# for num in different:
#     i = array_a.index(num)
#     right = array_a[:i]
#     # if i != n-1:
#     left = array_a[i+1:]
#     # else:
#     #     left = None
#     print(right)
#     print(left)

# for i in range(n):
#     if array_a[i] == array_b[i]:
#         count = array_b.count(array_a[i])
#         if count > 1:
#             if array_a[i] != array_b[i+1]:
#                 while True:
#                     newsame = []
#                     list = array_a[:i+1]+array_a[i]
#                     for j in range(n):
#                         if n 
#                         newsame.append(n)
#                     if len(n) > len()
