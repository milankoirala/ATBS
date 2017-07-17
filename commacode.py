spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(spam):
    if spam: # prevent parsing an empty list
        return print(', '.join(spam[:-1]) + ', and ' + spam[-1])

print('The original spam list.')
print(spam)

commaCode(spam)

   