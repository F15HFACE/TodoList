import streamlit as st
import functions as fn

def add_todo():
    todo=st.session_state['newtodo']+'\n'
    todos=fn.get_todos()
    todos.append(todo)
    fn.write_todos(todos)


todos = fn.get_todos()
st.title('Get on with it')

for todo in todos:
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='',placeholder='Add a new one',
              on_change=add_todo, key='newtodo')

