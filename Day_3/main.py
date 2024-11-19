from function import get_todos, write_todos
import time

now = time.strftime("%b-%d-%y-%H-%M-%S")
print("It is", now)

while True:
    user_action = input("Enter add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos("todos.txt")

        todos.append(todo)

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):  # for loop
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")
            index = number - 1

            to_do_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos("todos.txt", todos)

            message = f"Todo {to_do_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
