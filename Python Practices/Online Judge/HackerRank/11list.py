if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command = input().split()
        operation = command[0]
        args = command[1:]

        if operation == 'insert':
            my_list.insert(int(args[0]), int(args[1]))
        elif operation == 'print':
            print(my_list)
        elif operation == 'remove':
            my_list.remove(int(args[0]))
        elif operation == 'append':
            my_list.append(int(args[0]))
        elif operation == 'sort':
            my_list.sort()
        elif operation == 'pop':
            my_list.pop()
        elif operation == 'reverse':
            my_list.reverse()


# The code above is a simple list manipulation program that takes a number of commands and performs operations on a list.
def func(N, commands):
    my_list = []

    for i in range(N):
        command = commands[i].split()
        operation = command[0]
        args = command[1:]

        if operation == 'insert':
            my_list.insert(int(args[0]), int(args[1]))
        elif operation == 'print':
            print(my_list)
        elif operation == 'remove':
            my_list.remove(int(args[0]))
        elif operation == 'append':
            my_list.append(int(args[0]))
        elif operation == 'sort':
            my_list.sort()
        elif operation == 'pop':
            my_list.pop()
        elif operation == 'reverse':
            my_list.reverse()

    return my_list  # Return the list after all operations

if __name__ == '__main__':
  # input
  N = int(input())
  commands = []

  for _ in range(N):
      commands.append(input())

  # fun call
  func(N, commands)  # We no longer need print here
  
  