import streamlit as st
import os
from openai import OpenAI

# Настройка страницы
st.set_page_config(page_title="Мой ИИ Агент", page_icon="🤖")
st.title("🤖 Мой ИИ Агент")
st.caption("Работает на базе DeepSeek")

# Подключаем мозги DeepSeek
# Ключ мы будем брать из переменных окружения (Streamlit Secrets)
try:
    api_key = st.secrets["DEEPSEEK_API_KEY"]
except Exception:
    # Если запускаете локально, можно использовать os.getenv
    api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

# Инициализация истории чата
if "messages" not in st.session_state:
    st.session_state.messages = []

# Отображение истории сообщений
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Поле ввода для пользователя
if prompt := st.chat_input("Напиши что-нибудь..."):
    # Добавляем сообщение пользователя в историю
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Получаем ответ от DeepSeek
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Запрос к модели
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True
        )
        
        # Стриминг ответа (чтобы текст появлялся по буквам)
        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Сохраняем ответ ассистента в историю
    st.session_state.messages.append({"role": "assistant", "content": full_response})
