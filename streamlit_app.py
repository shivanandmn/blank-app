import streamlit as st

# Include custom CSS for styling the camera input
st.markdown(
    """
    <style>
    /* Force the camera input to full width and height on mobile */
    video {
        width: 100vw !important;
        height: 100vh !important;
        object-fit: cover !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Camera input to capture an image
img = st.camera_input("Take a picture")

if img:
    st.image(img)
