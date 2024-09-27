import streamlit as st

# File uploader to allow the user to upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("File Uploaded successfully!")
else:
    st.write("Please upload an image file.")
