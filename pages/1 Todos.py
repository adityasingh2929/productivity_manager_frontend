# import streamlit as st
# import apis.todo_api as api


# st.title("Daily Todos:")
# st.write(" ")
# st.write(" ")
# st.write(" ")

# # setting an 'editing_id' attribute in session_state which'll later be used to update todos.
# if "editing_id" not in st.session_state:
#     st.session_state.editing_id = None


# # Showing the todo's here (each of your todo's will have the option for update and delete.)
# st.subheader("Todos for the day: ")
# ctr = 1
# todos = api.get_todos()
# if todos:
#     values = [todo['todo_detail'] for todo in todos]
#     ids = [number['id'] for number in todos]

#     for itr,each in enumerate(values):
#         col1,col2,col3 = st.columns(3)

#         with col1:
#             st.checkbox(f"{each}", key=ids[itr])

#         with col2:
#             if st.button(f"Update", key=f"update{ids[itr]}"):
#                 # clicking on update hence now we're storing todo id to remember it for the next button press.
#                 st.session_state.editing_id = ids[itr]

#             if st.session_state.editing_id == ids[itr]:
#                 update_input = st.text_input('Update the todo: ', key=f"update_input_of_{ids[itr]}")

#                 if st.button("Submit update",key=f"submit_update_{ids[itr]}"):
#                     res = api.update_todo(ids[itr],update_input)
#                     if res:
#                         st.success("Updation successful")
#                     else:
#                         st.error("Updation failed!")

#                     # reset state
#                     st.session_state.editing_id = None
#                     st.rerun()

#         with col3:
#             if st.button(f"Delete", key=f"delete{ids[itr]}"):
#                 res = api.delete_todo(ids[itr])
#                 if res:
#                     st.success("Deleted")
#                 else:
#                     st.error("Deletion failed")
#                 st.rerun()

# st.write(" ")
# st.write(" ")
# st.write(" ")

# # Creating todos
# st.subheader("Create a todo: ")
# todo_input = st.text_input('Enter to submit')

# if st.button("Add todo"):
#     if todo_input:
#         api.create_todo(todo_input)
#         st.success("Todo added")
#         st.rerun()
#     else:
#         st.warning("Cannot be empty")





# # Logic:
# # No id no. of the todos will be shown, User'll have nothing to do with it, its just something that'll be used in the backend for update and deletion.
