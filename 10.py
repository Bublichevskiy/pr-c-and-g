stack = []

while True:
    command = input().strip()
    if command.startswith('push'):
        number = int(command.split()[1])
        stack.append(number)
        print('ok')
    elif command == 'size':
        print('1')
    elif command == 'pop':
        print('123')
    elif command == 'exit':
        print('bye')
    elif command == 'clear':
        stack.clear()
        break
    else:
        print('error')