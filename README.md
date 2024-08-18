# AI-Buddha 
AI chat with Buddha based on early Buddhism(초기불교에 근거한 AI 부처님 챗봇)

이 프로젝트는 제 관심사와 필요에 따라 진행했습니다.

chat-gpt를 활용하여 가상의 부처님과 대화하는 분이 있다고 전해들었습니다. 자신의 고민의 내용을 상세한 설명을 통해 물어보면, 실제 스님들이 대답하는 것과 유사한 느낌이어서 꽤 유용하겠다 싶었습니다.

이미 상용화된 AI-부처 챗봇이 존재하지만, 초기불교에 근거한 부처님은 없습니다. 대부분의 종교가 그렇듯이, 시간이 흐르며 불교 또한 다양하게 발전하였습니다. 저는 그 중에서도 '**초기불교**' 즉, '부처님의 살아생전의 말씀을 담은 '니까야 경전'에 담긴 내용을 근거로한 불교'에 관심이 많습니다. 

그래서 좀 더 맞춤 프로폼트를 통해서 초기불교 AI부처님을 만들어봐야겠다고 생각했습니다.

## 0. Preview

![image](https://github.com/user-attachments/assets/08b4d694-7e57-414f-86f7-a2119e5e8114)


## 1. Install

### prerequisite
> * python3.9 이상
> * streamlit
> * openai
> * gcloud CLI, SDK
> * google.cloud.secretmanager

```
#구글 클라우드 sdk 설치
https://cloud.google.com/appengine/docs/flexible/setting-up-environment?tab=python&hl=ko

#openAI-API KEY를 비밀키로 저장하기 위하여 google cloud secret manager 사용
(https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets?hl=ko)

#라이브러리 설치
pip install -r requirements.txt
```
#### A. 로컬 배포
```
streamlit run app.py
```
#### B. 구글 클라우스 배포
```
#구글 클라우드 앱엔진 프로젝트 설정 및 앱 배포
gcloud config set project [PROJECT_ID]
gcloud app create --region=asia-northeast3
gcloud app deploy
gcloud app browse
```

## 2. 오버뷰

![image](https://github.com/user-attachments/assets/853beb91-a724-46c0-8393-722bffbb12bf)


Streamlit에서 chatbot web화면을 제공해주었기 떄문에, 프론트 구성이 편리했다.

로컬배포만이 아니라 remote 서버에 배포까지 해보고 싶어서 Google Cloud Platform을 사용했다.

앱 배포가 바로 가능한 APP ENGINE서비스를 사용했다.


## 3.git commit 메시지 규약
> * ➕ FEAT: 새로운 기능 추가
> * ❗ FIX: 버그 수정
> * 📝 DOCS: 문서 수정
> * 🎨 STYLE: 스타일 관련 기능(코드 포맷팅, 세미콜론 누락, 코드 자체의 변경이 없는 경우)
> * ⬆️ REFACTOR: 코드 리팩토링
> * 🔎 TEST: 테스트 코드 추가
> * ⚙ CHORE: 빌드 업무 수정, 패키지 매니저 수정(ex .gitignore 수정 같은 경우)

제목을 넘어, 본문 작성 필요시 '어떻게' 변경했는지 보다 '무엇을, 왜' 변경했는지 작성한다.



## 4. 이슈 및 해결

### 4-1. 앱 배포 후, 브라우저 접속 시 무한 wait
리모트 서버인 Google Cloud Platform 의 앱엔진을 사용하여 앱을 배포하였는데, 브라우저에서 화면이 로드되지 않고 무한 wait 발생. 클라이언트에서 GET 요청 시 'GCP APP 웹소켓 에러' 발생.
확인해 보니 GCP의 앱 엔진에서 ["표준 환경/가변형 환경"](https://cloud.google.com/appengine/docs/the-appengine-environments?hl=ko) 을 선택해서 앱을 실행하는데, "표준 환경"에서는 **WebSocket기능**을 사용할 수 없었다. streamlit의 chat기능은 실시간 대화를 제공하므로 HTTP통신이 아닌 WebSocket방식을 사용하고 있었다.
앱 엔진의 환경을 "가변형 환경"으로 실행하여 문제 해결.

### 4-2. 프롬포트 노출 문제
chat GPT에게 AI-부처 역할을 부여하는 프롬포트가 유저에게 보여지는 문제 발생. 세션에 저장되어 있는 모든 메세지를 화면에 로드하기 때문에 발생하였다.
Message의 role이 "System"일 경우에는 메세지 로드하지 않는 제어로직 추가.


## 5. 개선할 점

### 5-1. Google Cloud Platform APP ENGINE 배포시 시간 지연 
"가변형 환경"으로 앱 배포시 "표준 환경"으로 배포 시보다 10배 정도 오래걸린다(약 10~20분). 시간을 줄일 수 있는 방법 모색 필요.
 
### 5-2.프롬포트 업데이트
내가 원하는 스타일의 대답이 나오려면 상세하게 알려주는 것이 필요하다. 불교의 내용이 매우 방대하고, 그 중 초기불교식의 대답을 만들어야하기 때문에, 어떤 경에 근거해서 말해야 하는지와 어떤 개념을 핵심으로 하여 대답하여야 할지 말해주어야 한다.
대답의 형식도 구성하여 알려주어야 한다. 
어느정도는 완성되었지만, chat GPT에게 '무상,고,무아'의 지혜를 활용해서 답변을 해달라고 했음에도 디테일이 부족했다. 해당 지혜들이 질문자의 상황에서 어떻게 적용되어 도움이 될지, 스님의 대답보다 와닿지가 않았다.
스님들의 문답을 더 자세히 듣고, chat GPT에게 요청할 필요가 있다.

