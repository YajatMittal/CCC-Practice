params = input().split(" ")
T = int(params[0])
N = int(params[1])
answers = []
for word in range(T):
    word = input()
    word_list = []
    for letter in word:
        word_list.append(letter)
    letter_types = []
    cases = 0

    for i in range(N):
        temp_word_list = [letter for letter in word_list]
        letter = word_list[i]
        temp_word_list.pop(i)
        if letter in temp_word_list:
            letter_types.append("heavy")
        else:
            letter_types.append("light")
    
    for i in range(len(letter_types)):

        if i != len(letter_types) - 1:
            if letter_types[i] != letter_types[i+1]:     
                cases += 1
        else:
            if letter_types[i] != letter_types[i-1]:
                cases += 1

    if cases == len(letter_types):
        answers.append("T")
    else:
        answers.append("F")

for ans in answers:
    print(ans)