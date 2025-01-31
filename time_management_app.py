import streamlit as st
import time
import pandas as pd

# Set page config
st.set_page_config(page_title="Time Manager", page_icon="⏳", layout="centered")
st.markdown("""
    <style>
        body {
            background-color: white;
            color: black;
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: black;
            color: white;
            border-radius: 5px;
            width: 100%;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("⏳ Simple Time Manager")

task_name = st.text_input("Task Name", "")
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "time_log" not in st.session_state:
    st.session_state.time_log = []
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0

if st.button("Start Timer"):
    st.session_state.start_time = time.time()
    st.session_state.elapsed_time = 0
    st.success("Timer started!")

if st.session_state.start_time:
    st.session_state.elapsed_time = round(time.time() - st.session_state.start_time, 2)
    st.write(f"### Timer: {st.session_state.elapsed_time} seconds")
    time.sleep(1)
    st.experimental_rerun()

if st.button("Stop Timer") and st.session_state.start_time:
    end_time = time.time()
    duration = round(end_time - st.session_state.start_time, 2)
    st.session_state.time_log.append({"Task": task_name, "Duration (s)": duration})
    st.session_state.start_time = None
    st.success(f"Task '{task_name}' logged: {duration} seconds")

# Display time log
df = pd.DataFrame(st.session_state.time_log)
if not df.empty:
    st.write("## Time Log")
    st.dataframe(df)
    
    # Download log
data_csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download Log", data_csv, "time_log.csv", "text/csv")

