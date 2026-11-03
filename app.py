import streamlit as st

st.title('streamlit App')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a text')
st.write('This is also a text using write function')

user_input = st.text_input('Write your text here')
st.write(user_input)

number_input = st.number_input('Enter a number')
st.write('Entered number:', number_input)


file_upload = st.file_uploader('Upload  your file')
st.button('Submit')
choici = st.radio('Choose an option', ['Yes', 'No'])

image_captured= st.camera_input('Smile Please')
st.image(image_captured)
st.write(":rainbow[this is a rainbow text]")
st.write(":blue[This is a blue text]")              