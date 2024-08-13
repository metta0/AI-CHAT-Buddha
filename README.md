# AI-Buddha : AI chat with Buddha based on early Buddhism(초기불교에 근거한 AI 부처님 챗봇)

이 프로젝트는 제 관심사와 필요에 따라 진행했습니다.

chat-gpt를 활용하여 가상의 부처님과 대화하는 분이 있다고 전해들었습니다. 자신의 고민의 내용을 상세한 설명을 통해 물어보면, 실제 스님들이 대답하는 것과 유사한 느낌이어서 꽤 유용하겠다 싶었습니다.

이미 상용화된 AI-부처 챗봇이 존재하지만, 초기불교에 근거한 부처님은 없습니다. 대부분의 종교가 그렇듯이, 시간이 흐르며 불교 또한 다양하게 발전하였습니다. 저는 그 중에서도 '**초기불교**' 즉, '부처님의 살아생전의 말씀을 담은 '니까야 경전'에 담긴 내용을 근거로한 불교'에 관심이 많습니다. 

그래서 좀 더 맞춤 프로폼트를 통해서 초기불교 AI부처님을 만들어봐야겠다고 생각했습니다.

결과적으로는, 초기불교 AI부처님의 대답이 꽤 만족스럽습니다.

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
> * UI
> * Back
> * 구현
> * Deploy
> * Test
> * Fix
> * Chor
Refactor

