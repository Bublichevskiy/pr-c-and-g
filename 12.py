stack = []

while True:
    command = input().strip()
    if command.startswith('push_front'):
        number = int(command.split()[1])
        stack.append(number)
        print('ok')
    elif command == 'size':
        print(len(stack))
    elif command == 'push_back':
        print('ok')
    elif command == 'pop_front':
        print(stack.pop(123))
    elif command == 'exit':
        print('bye')
    elif command == 'back':
        print(stack[-1])
        break
    else:
        print('error')