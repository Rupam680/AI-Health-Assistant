import streamlit as st

st.title("AI Health Assistant 🩺")
report = st.text_area("Medical Report Input")

if st.button("Analyze"):
    st.subheader("AI Health Analysis Result")

    report_lower = report.lower()

    
    if "chest pain" in report_lower or "bp" in report_lower or "heart" in report_lower:
        st.write("1. Possible Heart Disease Risk")
    
    if "stress" in report_lower or "anxiety" in report_lower or "sleep" in report_lower:
        st.write("2. Anxiety or Mental Stress Disorder")

    if "cough" in report_lower or "breath" in report_lower or "asthma" in report_lower:
        st.write("3. Lung or Breathing Disorder")

    if report.strip() == "":
        st.write("Please enter a medical report.")

    st.warning("⚠ This is AI-assisted preliminary diagnosis. Consult a doctor.")
