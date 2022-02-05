



from string import ascii_letters as alpha
def atbash(txt):
	return txt.translate(str.maketrans(alpha,alpha[::-1].swapcase()))


# def get_opposite(char):
#     if char.isalpha():
#         if (char.isupper()):
#             offset = ord(char) - ord('A')
#             return chr(ord('Z') - offset)
#         else:
#             offset = ord(char) - ord('a')
#             return chr(ord('z') - offset)
#     else:
#         return char

# def atbash(txt):
#     ret = []
#     for letter in txt:
#         ret.append(get_opposite(letter))
#     return ''.join(map(str, ret))

print (atbash("Christmas is the 25th of December"))


