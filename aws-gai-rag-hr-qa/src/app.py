import streamlit as st
import rag_backend as demo

st.set_page_config(page_title="HR Q and A with RAG")  # Modify Heading

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">HR Q&A with RAG</p>'
st.markdown(new_title, unsafe_allow_html=True)  # Modify Title

if "vector_index" not in st.session_state:
    with st.spinner("📀 Wait for magic...All beautiful things in life take time :-)"):  # Spinner message
        st.session_state.vector_index = demo.create_hr_index()  # Index Function name from Backend File

input_text = st.text_area("Input text", label_visibility="collapsed")
go_button = st.button("📌Ask your company chat assistant", type="primary")  # Button Name

if go_button:

    with st.spinner("📢Anytime someone tells me that I can't do something, I want to do it more - Taylor Swift"):  # Spinner message
        response_content = demo.get_hr_rag_response(index=st.session_state.vector_index, question=input_text)  # Replace with RAG Function from backend file
        st.write(response_content)
