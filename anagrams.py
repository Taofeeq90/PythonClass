input_string = input('Enter a list of words you would like check for anagrams separated by space ')
print("\n")
word_list = input_string.split()

def freq(word):
    freq_dict = {}
    for char in word:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict
# initialize a list
anagram_list = []
#not_anagram_list = []
for word_1 in word_list: 
    for word_2 in word_list: 
        if word_1 != word_2 and (freq(word_1) == freq(word_2)):
            anagram_list.append(word_1)
            print (word_1, "and", word_2, "are anagram of each other" )
        else:
            #not_anagram_list.append(word_1)
            print (word_1, "and" , word_2, "are not anagram of each other" )
            
print(anagram_list)
print(not_anagram_list)

# Example Proof
print (" Here is the proof ")
print ("Dictionary: ")
print(freq(word_list[0]))
print(freq(word_list[1]))

print ("List: ")
print (sorted(list(freq(word_list[0]).items())))
print (sorted(list(freq(word_list[1]).items())))