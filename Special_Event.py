n = int(input())
availibilities = []
days = {"1":0, "2":0, "3":0, "4":0, "5":0}
highest_day = 0
available = ''


for people in range(0,n):
    availibility = input()
    availibilities.append(availibility)

for i in range (0,len(availibilities)):
    day_num = 0
    for option in availibilities[i]:
        day_num += 1
        if option == "Y":
            days[str(day_num)] += 1
            

for d in days:
    if days[d] > highest_day:     
        available = d
        highest_day = days[d]

    elif days[d] == highest_day:
        available += "," + d
 
print(available)