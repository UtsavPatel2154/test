name = 'utsav'
password = '123'

if name == 'utsav' and password == '123':
    print('Welcome', name)
elif name != 'utsav' and password == '123':
    print('Invalid username')
elif name == 'utsav' and password != '123':
    print('Invalid password')
else:
    print('Invalid username or password')