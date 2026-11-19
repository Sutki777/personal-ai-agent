
import streamlit as st

st.set_page_config(
    page_title="Personal AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Personal AI")
st.caption("Твой личный интеллектуальный помощник")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Напиши своему помощнику...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    answer = (
        "Привет! Я твой Personal AI. "
        "Сейчас мы создаём мои возможности. "
        "Скоро я смогу помогать тебе с разными задачами!"
    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()
