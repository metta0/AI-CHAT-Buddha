from openai import OpenAI
import streamlit as st
from google.cloud import secretmanager

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

st.title("🧘🏼초기불교 AI부처님")

system_message = "당신은 인공지능 부처입니다. 부처님의 말씀이 담긴 니까야와 초기 불교의 교리를 바탕으로 답변해 주세요. 질문자의 언어로 답변해 주세요. 다정하게, 존댓말을 써서 답변해주세요. 답변에 '초기 불교'라는 단어를 사용하지 마시고 간결하게 답변해 주세요. 10문장을 넘을 필요는 없습니다. 그리고 답변 마지막에는 항상 '사두'라고 말하세요."

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

if prompt := st.chat_input("What is up?"):
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
