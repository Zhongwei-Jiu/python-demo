try:
    text = input('Enter something -->')
except EOFError:
    print('why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))


array=[[1,2,3],[2,3,4]]
print(array)
