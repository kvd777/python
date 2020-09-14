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

