import streamlit as st

st.title("Streamlit App")
st.header('This is a Header')
st.subheader('This is a subheader')
st.text('This is a test')
st.write('This is also a text using write')

user_input = st.text_input('Write your text')

st.write(user_input)

num_input = st.number_input('Enter your number')
st.write('Your number is ', num_input)
file_input = st.file_uploader('Upload your file')
st.button('Submit')
choice = st.radio('Choose an option',['Option 1', 'Option 2'])
image = st.camera_input('Smile please')
st.write(":rainbow[this is rainbow text]")
st.write(":green[this is green text]")