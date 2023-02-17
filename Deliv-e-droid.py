p = int(input())
c = int(input())
score = (50*p) - (c*10)
if p > c:
    score += 500

print(score)