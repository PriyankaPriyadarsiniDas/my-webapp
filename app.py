import streamlit as st

# App title
st.title("My Interactive Web App")
st.subheader("Welcome! Please fill in your details below:")

# Input fields
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=120)
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
hobby = st.text_input("Enter your favorite hobby")

# Submit button
if st.button("Submit"):
    st.success(f"Hello, {name}!")
    st.write(f"- Age: {age}")
    st.write(f"- Gender: {gender}")
    st.write(f"- Hobby: {hobby}")
    st.write("Glad to have you here! 😊")

# Optional fun section
if st.checkbox("Show a fun message"):
    st.balloons()
    st.write("🎉 Enjoy using this app! 🎉")