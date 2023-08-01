word = input()
r_word = ''.join(reversed(word))
if word == r_word:
    print(1)
else:
    print(0)