stack = []

while True:
    command = input().strip()
    if command.startswith('push'):
        number = int(command.split()[1])
        stack.append(number)
        print('ok')
    elif command == 'size':
        print(len(stack))
    elif command == 'exit':
        print('bye')
        break
    else:
        print('error')