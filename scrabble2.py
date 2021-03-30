import click

score = {}


if click.confirm('Type YES to use default dictionary or NO to create custom dictionary:', default=True):
    with open("default-dict.txt") as f:
        for line in f:
            (key, val) = line.split()
            score[key] = int(val)
    print(score)

else:
    for i in range(26):
        data = input('Enter letter & score separated by space: ').split(' ')
        score[data[0]] = int(data[1])

print(score)

input_string = input('Enter your scrabble word to get total score: ')
print("\n")
#Method1 using lambda function
scrabble_score = lambda word: sum([score[l] for l in word.lower()])

print(scrabble_score(input_string))


