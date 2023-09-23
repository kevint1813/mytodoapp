import streamlit as st
import functions

todos = functions.getlist()
def add_todo():
    todo = st.session_state["addtodo"]
    todos.append(todo + "\n")
    functions.writelist(todos)


st.title("This is a ToDo Web App.")
st.subheader("developed by Kevin T.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.writelist(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="enter a todo...", key="addtodo", on_change=add_todo)

