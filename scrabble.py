score = {}
with open("default-dict.txt") as f:
    for line in f:
        (key, val) = line.split()
        score[key] = int(val)

#print(score)
input_string = input('Enter your scrabble word to get total score: ')
print("\n")
#Method1 using lambda function
scrabble_score = lambda word: sum([score[l] for l in word.lower()])
# Method2
"""def scrabble_score(word):
    total = 0
    for i in word:
        total = total+score[i.lower()]
    return total"""
#Method3    
"""def scrabble_score(word):
   return sum(score[letter] for letter in word.lower())"""
print(scrabble_score(input_string))