def get_todos(filepath):
    """Read a text file and return the list
    of to-do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todo_arg):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todo_arg)


 # print(__name__)   """prints the name of this file: function
 #                       when it is called in another module and
 #                       prints __main__ in this file.
 #                       """


if __name__ == "__main__":
    print("some thing.")  # avoids the execution of this function
