n = int(input())
peppers = {"Poblano":1500, "Mirasol":6000, "Serrano":15500, "Cayenne":40000, "Thai":75000, "Habanero":125000}
spiciness = 0
for name in range(0,n):
    pepper_name = input()
    spiciness += peppers[pepper_name]

print(spiciness)
