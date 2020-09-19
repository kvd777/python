# Kane's solution:
word = input()
password = ''
count = 0

key = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'
    }

while count < len(word):
    for char in word:
        if char in key:
            new_char = char.replace(char,key[char])
            print(new_char,end='')
            count += 1
        else:
            print(char, end='')
            count += 1
    if count == len(word):
        print('q*s')


# -------------------------------------------------------
# Doug's solution:
# Here's another way to solve the passwrod modifier problem
# Instead of looping over the word, we loop over the
# cypher keys
word = input()

pass_map = {
    'i': '!',
    'a': '@',
    'm': 'M',
    'B': '8',
    'o': '.'
}

# .items method returns a tuple with key, value as the 2 elements
for txt, repl in pass_map.items():
    word = word.replace(txt, repl)

print(word + 'q*s')
