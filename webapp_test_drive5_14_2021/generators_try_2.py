data = [1, 2, 3, 4, 5, 6, 7, 8]

# Ordinary loop
evens_loop = []
for num in data:
    if not num % 2 == 0:
        evens_loop.append(num)

# Generator
evens = [num for num in data if not num % 2]

# Ordinary loop
data = [1, 'One', 2, 'Two', 3, 'Three', 4, 'Four']
words_loop = []
for num in data:
    if isinstance(num, str):
        words_loop.append(num)

# Generator
words = [num for num in data if isinstance(num, str)]

# Ordinary loop
data = list('So long and thanks for all the fish'.split())
title_loop = []
for word in data:
    title_loop.append(word.title())

# Generator
title = [word.title() for word in data]


'''Loop and generator to revert a list'''

# Loop to revert a list
a_list = [1, 'Two', 3, 4, 'Five', 6.0]
print(a_list)

reverted_list = []
for index in range(len(a_list)-1, -1, -1):
    reverted_list.append(a_list[index])

print(reverted_list)

# complete later not sure that this is possible
#reverto_del_listo = [for index in range(len(a_list)-1, -1, -1) ]

