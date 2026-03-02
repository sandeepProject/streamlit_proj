import streamlit as st
with st.sidebar:
    st.header('This is side bar')
    st.image("https://techicons.dev/icons/anaconda",width=100)
messages = st.container()
if prompt := st.chat_input('Say something'):
    messages.chat_message('user').write(prompt)
    messages.chat_message('assistant').write(f'Echo: {prompt}')
    
#https://share.streamlit.io
#Using render
    #pip install -r requirements.txt
    #streamlit run app.py --server.port $PORT --server.address 0.0.0.0
