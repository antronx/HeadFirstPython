vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")
found = {}


for letter in word:
    if letter not in found:
        found[letter] = 0
    found[letter]+=1
print(found)
for key, value in sorted(found.items()):
    print(key,' was found ', value, ' times.')
        
