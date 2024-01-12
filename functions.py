FILEPATH = 'todos.txt'

def get_todos(filepath =  FILEPATH):
    '''Opens file FILEPATH and writes contents to list which is returned'''
    with open(filepath) as local_todofile:
        todos_local = local_todofile.readlines()
    return todos_local

def write_todos(local_todos, filepath = FILEPATH):
    '''takes a list and writes to file FILEPATH'''
    with open(filepath, 'w') as local_todofile:
        local_todofile.writelines(local_todos)
