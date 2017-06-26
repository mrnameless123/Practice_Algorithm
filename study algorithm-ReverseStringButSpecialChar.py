import string

norm_char = string.digits + string.ascii_letters
mystring =  input().strip()
reverse_letter = [c for c in mystring[::-1] if c in norm_char]
[reverse_letter.insert(mystring.index(c),c) for c in mystring if c not in norm_char]
print(''.join(reverse_letter), sep=' ')