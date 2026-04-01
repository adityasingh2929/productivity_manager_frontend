#-----------------------------------------------------------------------

import streamlit as st
from apis import gymlogs_api as api
from typing import Dict
from pydantic import BaseModel

st.title("GYM LOGS")

if "adding_id" not in st.session_state:
    st.session_state.adding_id = None
if "editing_id" not in st.session_state:
    st.session_state.editing_id = None
if "week_exists" not in st.session_state:
    st.session_state.week_exists = None

if st.button("Create new gymweek", key="gymweek creation"):
    week = api.create_week()
    if week:
        st.success("new week created!")
    st.rerun()

weeks = api.fetch_week()
if weeks:
    weeks_processed = [week["week_number"] for week in weeks]
week_number_selected = st.selectbox("Week number: ",[week_number for week_number in weeks_processed])
# st.write(week_number_selected)

if week_number_selected:

    col1, col2 = st.columns(2)

    chest = "chest"
    back = "back"
    arms = "arms"
    legs = "legs"

    with col1:
        
        st.subheader(chest)
        chest_log_selected = st.selectbox(chest,["Inclined db press", "Machine flat press", "Machine chest flys"], key="chest_selectbox")
        if chest_log_selected:
            response = api.fetch_logs(week_number_selected,chest_log_selected)
            if response:
                    for individual_record in response:
                        id = individual_record["id"]
                        c1,c2,c3 = st.columns(3)
                        with c1:
                            st.success(f"{individual_record["weight"]}kgs : {individual_record["reps"]} reps (SET={individual_record["set"]})")
                        with c2:
                            if st.button("update", key=f"chest_updating: {id}"):
                                st.session_state.editing_id = id
                            if st.session_state.editing_id == id:
                                update_workout_type = st.text_input("enter workout type for update", key=f"chest_type {id}")
                                update_workout_name = st.text_input("enter workout name for update", key=f"chest_name {id}")
                                update_weight = st.text_input("enter weight for update", key=f"chest_weight {id}")
                                update_reps = st.text_input("enter reps for update", key=f"chest_reps {id}")
                                update_set = st.text_input("enter set for update", key=f"chest_set {id}")
                                if st.button("submit",key=f"chest_submit {id}"):

                                    update_workout_type = update_workout_type or None
                                    update_workout_name = update_workout_name or None
                                    update_weight = update_weight or None
                                    update_weight = update_weight or None
                                    update_reps = update_reps or None
                                    update_set = update_set or None

                                    response = api.update_logs(id,update_workout_type,update_workout_name,update_weight,update_reps,update_set)
                                    if response:
                                        st.session_state.editing_id = None
                                        st.rerun()

                        with c3:
                            if st.button("delete", key=f"chest_deleting: {id}"):
                                response = api.delete_logs(id)
                                if response:
                                    st.rerun()

                    if st.button("Add log",key="chest_add_log"):
                        st.session_state.adding_id = True

                    if st.session_state.adding_id == True:
                        chest_workout_weight = st.text_input("Enter weight (in kgs)", key="chest_addlog_weight")
                        chest_workout_reps = st.text_input("Enter reps (r/l)", key="chest_addlog_reps")
                        chest_workout_set = st.text_input("Enter set number", key="chest_addlog_set_number")
                        if st.button("Submit",key="chest_submit"):
                            response = api.add_logs(week_number_selected,chest,chest_log_selected,chest_workout_weight,chest_workout_reps,chest_workout_set)
                            st.session_state.adding_id = None
                            if response:
                                st.rerun()
                # Exception code for if the selected workout has no log
            else:
                st.info("No workout log present")
                if st.button("Add log",key="chest_add_log_else"):
                        st.session_state.adding_id = True

                if st.session_state.adding_id == True:
                    chest_workout_weight = st.text_input("Enter weight (in kgs)", key="chest_addlog_weight")
                    chest_workout_reps = st.text_input("Enter reps (r/l)", key="chest_addlog_reps")
                    chest_workout_set = st.text_input("Enter set number", key="chest_addlog_set_number")
                    if st.button("Submit",key="chest_submit_else"):
                        response = api.add_logs(week_number_selected,chest,chest_log_selected,chest_workout_weight,chest_workout_reps,chest_workout_set)
                        st.session_state.adding_id = None
                        if response:
                            st.rerun()
                    
                


        st.subheader(arms)
        arms_log_selected = st.selectbox(arms,["Triceps pushdown","triceps overhead extensions","machine preacher biecp curls","preacher bicep hammer curl","cable lateral raises (unilateral)","machine shoulder press"], key="arms_log_selected")
        if arms_log_selected:
            response2 = api.fetch_logs(week_number_selected,arms_log_selected)
            if response2:
                    for individual_record in response2:
                        id = individual_record["id"]
                        c1,c2,c3 = st.columns(3)
                        with c1:
                            st.success(f"{individual_record["weight"]}kgs : {individual_record["reps"]} reps (SET={individual_record["set"]})")
                        with c2:
                            if st.button("update", key=f"arms_updating: {id}"):
                                st.session_state.editing_id = id
                            if st.session_state.editing_id == id:
                                update_workout_type = st.text_input("enter workout type for update", key=f"arms_type {id}")
                                update_workout_name = st.text_input("enter workout name for update", key=f"arms_name {id}")
                                update_weight = st.text_input("enter weight for update", key=f"arms_weight {id}")
                                update_reps = st.text_input("enter reps for update", key=f"arms_reps {id}")
                                update_set = st.text_input("enter set for update", key=f"arms_set {id}")
                                if st.button("submit",key=f"arms_submit {id}"):

                                    update_workout_type = update_workout_type or None
                                    update_workout_name = update_workout_name or None
                                    update_weight = update_weight or None
                                    update_weight = update_weight or None
                                    update_reps = update_reps or None
                                    update_set = update_set or None

                                    response = api.update_logs(id,update_workout_type,update_workout_name,update_weight,update_reps,update_set)
                                    if response:
                                        st.session_state.editing_id = None
                                        st.rerun()

                        with c3:
                            if st.button("delete", key=f"arms_deleting: {id}"):
                                response = api.delete_logs(id)
                                if response:
                                    st.rerun()

                    if st.button("Add log", key="arms_add_log"):
                        st.session_state.adding_id = True

                    if st.session_state.adding_id == True:
                        arms_workout_weight = st.text_input("Enter weight (in kgs)", key="arms_addlog_weight")
                        arms_workout_reps = st.text_input("Enter reps (r/l)", key="arms_addlog_reps")
                        arms_workout_set = st.text_input("Enter set number", key="arms_addlog_set_number")
                        if st.button("Submit",key="arms_submit"):
                            response = api.add_logs(week_number_selected,arms,arms_log_selected,arms_workout_weight,arms_workout_reps,arms_workout_set)
                            st.session_state.adding_id = None
                            if response:
                                st.rerun()
                # Exception code for if the selected workout has no log
            else:
                st.info("No workout log present")
                if st.button("Add log",key="arms_add_log_else"):
                        st.session_state.adding_id = True

                if st.session_state.adding_id == True:
                    arms_workout_weight = st.text_input("Enter weight (in kgs)", key="arms_addlog_weight")
                    arms_workout_reps = st.text_input("Enter reps (r/l)", key="arms_addlog_reps")
                    arms_workout_set = st.text_input("Enter set number", key="arms_addlog_set_number")
                    if st.button("Submit",key="arms_submit_else"):
                        response = api.add_logs(week_number_selected,arms,arms_log_selected,arms_workout_weight,arms_workout_reps,arms_workout_set)
                        st.session_state.adding_id = None
                        if response:
                            st.rerun()
            




    with col2:
        st.subheader(back)

        back_log_selected = st.selectbox(back, ["Neutral grip lat pulldowns", "Wide grip t-bar kelso shrugs","back extensions","Rear delt flys"], key="back_log_selected")
        if back_log_selected:
            response3 = api.fetch_logs(week_number_selected,back_log_selected)
            if response3:
                for individual_record in response3:
                    id = individual_record["id"]
                    c1,c2,c3 = st.columns(3)
                    with c1:
                        st.success(f"{individual_record["weight"]}kgs : {individual_record["reps"]} reps (SET={individual_record["set"]})")
                    with c2:
                        if st.button("update", key=f"{back}_updating: {id}"):
                            st.session_state.editing_id = id
                        if st.session_state.editing_id == id:
                            update_workout_type = st.text_input("enter workout type for update", key=f"{back}_type {id}")
                            update_workout_name = st.text_input("enter workout name for update", key=f"{back}_name {id}")
                            update_weight = st.text_input("enter weight for update", key=f"{back}_weight {id}")
                            update_reps = st.text_input("enter reps for update", key=f"{back}_reps {id}")
                            update_set = st.text_input("enter set for update", key=f"{back}_set {id}")
                            if st.button("submit",key=f"{back}_submit {id}"):

                                update_workout_type = update_workout_type or None
                                update_workout_name = update_workout_name or None
                                update_weight = update_weight or None
                                update_weight = update_weight or None
                                update_reps = update_reps or None
                                update_set = update_set or None

                                response = api.update_logs(id,update_workout_type,update_workout_name,update_weight,update_reps,update_set)
                                if response:
                                    st.session_state.editing_id = None
                                    st.rerun()

                    with c3:
                        if st.button("delete", key=f"{back}_deleting: {id}"):
                            response = api.delete_logs(id)
                            if response:
                                st.rerun()

                if st.button("Add log", key=f"{back}_add_log"):
                    st.session_state.adding_id = True

                if st.session_state.adding_id == True:
                    back_workout_weight = st.text_input("Enter weight (in kgs)", key=f"{back}_addlog_weight")
                    back_workout_reps = st.text_input("Enter reps (r/l)", key=f"{back}_addlog_reps")
                    back_workout_set = st.text_input("Enter set number", key=f"{back}_addlog_set_number")
                    if st.button("Submit",key=f"{back}_submit"):
                        response = api.add_logs(week_number_selected,back,back_log_selected,back_workout_weight,back_workout_reps,back_workout_set)
                        st.session_state.adding_id = None
                        if response:
                            st.rerun()
            # Exception code for if the selected workout has no log
            else: 
                st.info("No workout log present")
                if st.button("Add log",key=f"{back}_add_log_else"):
                        st.session_state.adding_id = True

                if st.session_state.adding_id == True:
                    back_workout_weight = st.text_input("Enter weight (in kgs)", key=f"{back}_addlog_weight")
                    back_workout_reps = st.text_input("Enter reps (r/l)", key=f"{back}_addlog_reps")
                    back_workout_set = st.text_input("Enter set number", key=f"{back}_addlog_set_number")
                    if st.button("Submit",key=f"{back}_submit_else"):
                        response = api.add_logs(week_number_selected,back,back_log_selected,back_workout_weight,back_workout_reps,back_workout_set)
                        st.session_state.adding_id = None
                        if response:
                            st.rerun()
        
        

        st.subheader(legs)
        legs_log_selected = st.selectbox(legs,["Leg extensions","Seated hamstring curls","hip abductors","hip adductors","weighted calf raises"],key="legs_log_selected")
        if legs_log_selected:
            response4 = api.fetch_logs(week_number_selected,legs_log_selected)
            if response4:
                for individual_record in response4:
                    id = individual_record["id"]
                    c1,c2,c3 = st.columns(3)
                    with c1:
                        st.success(f"{individual_record["weight"]}kgs : {individual_record["reps"]} reps (SET={individual_record["set"]})")
                    with c2:
                        if st.button("update", key=f"{legs}_updating: {id}"):
                            st.session_state.editing_id = id
                        if st.session_state.editing_id == id:
                            update_workout_type = st.text_input("enter workout type for update", key=f"{legs}_type {id}")
                            update_workout_name = st.text_input("enter workout name for update", key=f"{legs}_name {id}")
                            update_weight = st.text_input("enter weight for update", key=f"{legs}_weight {id}")
                            update_reps = st.text_input("enter reps for update", key=f"{legs}_reps {id}")
                            update_set = st.text_input("enter set for update", key=f"{legs}_set {id}")
                            if st.button("submit",key=f"{legs}_submit {id}"):

                                update_workout_type = update_workout_type or None
                                update_workout_name = update_workout_name or None
                                update_weight = update_weight or None
                                update_weight = update_weight or None
                                update_reps = update_reps or None
                                update_set = update_set or None

                                response = api.update_logs(id,update_workout_type,update_workout_name,update_weight,update_reps,update_set)
                                if response:
                                    st.session_state.editing_id = None
                                    st.rerun()

                    with c3:
                        if st.button("delete", key=f"{legs}_deleting: {id}"):
                            response = api.delete_logs(id)
                            if response:
                                st.rerun()

                if st.button("Add log", key=f"{legs}_add_log"):
                    st.session_state.adding_id = True

                if st.session_state.adding_id == True:
                    legs_workout_weight = st.text_input("Enter weight (in kgs)", key=f"{legs}_addlog_weight")
                    legs_workout_reps = st.text_input("Enter reps (r/l)", key=f"{legs}_addlog_reps")
                    legs_workout_set = st.text_input("Enter set number", key=f"{legs}_addlog_set_number")
                    if st.button("Submit",key=f"{legs}_submit"):
                        response = api.add_logs(week_number_selected,legs,legs_log_selected,legs_workout_weight,legs_workout_reps,legs_workout_set)
                        st.session_state.adding_id = None
                        if response:
                            st.rerun()
            # Exception code for if the selected workout has no log
            else: 
                st.info("No workout log present")
                if st.button("Add log",key=f"{legs}_add_log_else"):
                        st.session_state.adding_id = True

                if st.session_state.adding_id == True:
                    legs_workout_weight = st.text_input("Enter weight (in kgs)", key=f"{legs}_addlog_weight")
                    legs_workout_reps = st.text_input("Enter reps (r/l)", key=f"{legs}_addlog_reps")
                    legs_workout_set = st.text_input("Enter set number", key=f"{legs}_addlog_set_number")
                    if st.button("Submit",key=f"{legs}_submit_else"):
                        response = api.add_logs(week_number_selected,legs,legs_log_selected,legs_workout_weight,legs_workout_reps,legs_workout_set)
                        st.session_state.adding_id = None
                        if response:
                            st.rerun()

# exception code for if the selected week has no workout log.
