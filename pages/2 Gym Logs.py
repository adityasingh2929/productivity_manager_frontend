import streamlit as st

st.title("GYM LOGS")

st.selectbox("Sessions: ",[ "ADD LOGS OF WEEK 5", "WEEK 1","WEEK 2", "WEEK 3", "WEEK 4"])   

col1, col2 = st.columns(2)

with col1:
    st.subheader("Day 1")
    
    st.selectbox("CHEST",["Inclined bench press", "Machine flat press", "Machine chest flys"])

    # if condition for records available:
        # create ui function call
    # else:
        # showing ui function call
        # if update called:
            #update ui function   (same as create funcion ui, just the button will be 'update' instead of add, and the text_input will have the pre-stored value fetched from the dbs.)
        # elif delte then:
            # create ui function call

    # create ui code:
    scol1,scol2 = st.columns(2)

    with scol1:
        st.text_input("Enter weight (in kgs)")
    with scol2:
        st.text_input("Enter reps (r/l)")
        st.button("Add")
    #--------------------------------------------

    st.subheader("Day 3")

    st.selectbox("ARMS",["Triceps pushdown","triceps overhead extensions","preacher bicep curls","preacher bicep hammer curl","cable lateral raises (unilateral)","machine shoulder press"])



with col2:
    st.subheader("Day 2")

    
    st.selectbox("BACK", ["Neutral grip lat pulldowns", "Wide grip t-bar kelso shrugs","back extensions","rear delt flys"])

    # show ui code:
    weight = 1
    reps = 1
    st.success(f"{weight} kgs - {reps} reps")
    s2col1,s2col2 = st.columns(2)
    with s2col1:
        st.button("update", key="update_fetchmode")
    with s2col2:
        st.button("delete", key="delete_fetchmode")
    

    st.subheader("Day 4")

    st.selectbox("LEGS",["Leg extensions","Leg curls","hip abductors","hip adductors","weighted calf raises"])
    


