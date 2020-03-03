#Banana scoring
def banana_points():
    three_pointers = bananas * 3
    field_goals = bananas  * 2
    free_throws = bananas * 1
    return  free_throws + field_goals +  three_pointers

#Apple scoring
def apple_points():
    three_pointers = apples  * 3
    field_goals = apples * 2
    free_throws = apples * 1
    return free_throws + field_goals +  three_pointers 

#Checking which team won
if banana_points() > apple_points():
   print('A') 

elif banana_points() < apple_points():
   print('B') 

elif banana_points() == apple_points():
   print('T') 
