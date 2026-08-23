import streamlit as st
from  transformer import pipeline
from PIP import images

#page settings 
st.set_page_config(
Page_title ="text generator",
page_icon="🤖"
)

st.title=("🔍 AI Object Detection")

detection=pipeline("object detection")

image=st.file_uploder(
" Upload an Image",
type=["jpg","png","jpeg"]
)

if image:
    image=image.open(image)
    st.image(img)
    if st.button("🔍 Detect objects"):
        result=detector(img)
        st.write(result)