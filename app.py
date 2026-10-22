import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Success System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Powered Student Success System")

st.write(
    "Identify students who may need academic support "
    "and provide personalized recommendations."
)

st.header("Enter Student Details")

name = st.text_input("Student Name")
attendance = st.slider("Attendance (%)", 0, 100, 75)
marks = st.slider("Average Marks (%)", 0, 100, 60)
assignments = st.slider("Assignments Completed (%)", 0, 100, 70)

if st.button("Analyze Student"):
    risk_score = (
        0.4 * (100 - attendance)
        + 0.4 * (100 - marks)
        + 0.2 * (100 - assignments)
    )

    st.subheader(f"Analysis for {name or 'Student'}")

    if risk_score >= 50:
        st.error("High academic risk: Additional support may be needed.")
        st.write("Recommendation: Arrange individual academic support.")
    elif risk_score >= 30:
        st.warning("Moderate academic risk: Monitor progress.")
        st.write("Recommendation: Provide practice exercises and feedback.")
    else:
        st.success("Lower estimated academic risk.")
        st.write("Recommendation: Continue current learning activities.")

    st.caption(
        "This is a preliminary rule-based estimate, not a trained AI model "
        "or a definitive assessment of student ability."
    )