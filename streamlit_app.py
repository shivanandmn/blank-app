import streamlit as st

# Custom CSS to make the camera full screen on mobile
st.markdown(
    """
    <style>
    /* This sets the video and canvas elements to full screen width */
    @media only screen and (max-width: 600px) {
        .stCameraInput div div div canvas, .stCameraInput div div div video {
            width: 100vw !important;
            height: auto !important;
        }
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Camera input to capture an image
img = st.camera_input("Take a picture")

if img:
    st.image(img)
