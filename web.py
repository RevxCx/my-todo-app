# local URL: http://localhost:8502
# Network URL: http://172.20.10.2:8502

import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    new_todo=st.session_state["new_todo"]
    print(todo)
    todos.append(new_todo+"\n")
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my To-Do app.")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()

user_input=st.text_input(label="",
              placeholder="Add a New Todo",
              on_change=add_todo,
              key="new_todo")