def is_palindrome(text):
    forbid=(' ','!','.',',','\'','"')
    for num in range(0,forbid.__len__()):
        if forbid[num] in text:
            text=text.replace(forbid[num],'')
    text=text.lower()
    reverse=text[::-1]
    return text==reverse



something = input('Enter something:')
if is_palindrome(something):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')
