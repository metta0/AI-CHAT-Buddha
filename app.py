from openai import OpenAI
import streamlit as st
from google.cloud import secretmanager

#chat_GPT 프롬프트 가져오기
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

gpt_prompt = load_text('prompt.txt')

##openai API KEY 가져오기
def get_secret(project_id: str, secret_id: str) -> str:

    client = secretmanager.SecretManagerServiceClient()
    secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"

    try:
        response = client.access_secret_version(name=secret_name)
        secret_value = response.payload.data.decode("UTF-8")
        return secret_value
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        return None

#AI Chatbot 시작
st.set_page_config(page_title="AI부처님", page_icon="🧘🏼")

st.title("🧘🏼 초기불교 AI부처님")

system_message = gpt_prompt

# Google Secret Manager에서 API 키를 가져옵니다.
api_key = get_secret("buddha-432307", "OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key could not be retrieved")

client = OpenAI(api_key=api_key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

if "system_message" not in st.session_state:
    st.session_state.system_message = {
        "role": "system",
        "content": system_message
    }

if "messages" not in st.session_state:
    st.session_state.messages = [st.session_state.system_message]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]) :
            st.markdown(message["content"])

if prompt := st.chat_input("무엇이든 물어보세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
