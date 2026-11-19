
import streamlit as st
from agent import PersonalAIAgent

st.set_page_config(
    page_title="Personal AI Agent",
    page_icon="🤖"
)

st.title("🤖 Personal AI Agent")
st.caption("Твой автономный интеллектуальный помощник")

agent = PersonalAIAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Поставь мне задачу...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    result = agent.run(prompt)

    answer = "План выполнения задачи:\n\n"

    for i, step in enumerate(result["steps"], 1):
        answer += f"{i}. {step}\n"

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()
