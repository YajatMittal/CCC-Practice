orignal_word = input()
result = input()
silly_key = ""
silent_key = ""
og_letter = ""
keys = ["","-"]
i = -1

for letter in orignal_word:
    if orignal_word.count(letter) != result.count(letter):
        if letter not in keys:
            i +=1
            keys[i] = letter

for letter in result:
    if letter not in orignal_word:
        og_letter = letter
for letter in orignal_word:
    count1 = orignal_word.count(keys[0]) + len(result)
    count2 = orignal_word.count(keys[1]) + len(result)
    if count1 == len(orignal_word):
        silent_key = keys[0]
        silly_key = keys[1]

    else:
        silent_key = keys[1]
        silly_key = keys[0]

print(silly_key + " " + og_letter)
print(silent_key)