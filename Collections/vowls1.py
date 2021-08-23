vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")
found = {'a':0,
         'e':0,
         'i':0,
         'o':0,
         'u':0
    }

for letter in word:
    if letter in vowels:
        #found[letter] = found[letter]+1
        found[letter]+=1
print(found)
for key, value in sorted(found.items()):
    print(key,' was found ', value, ' times.')
        
