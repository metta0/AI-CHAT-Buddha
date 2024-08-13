# AI-Buddha : AI chat with Buddha based on early Buddhism(초기불교에 근거한 AI 부처님 챗봇)

이 프로젝트는 제 관심사와 필요에 따라 진행했습니다.

chat-gpt를 활용하여 가상의 부처님과 대화하는 분이 있다고 전해들었습니다. 자신의 고민의 내용을 상세한 설명을 통해 물어보면, 실제 스님들이 대답하는 것과 유사한 느낌이어서 꽤 유용하겠다 싶었습니다.

이미 상용화된 AI-부처 챗봇이 존재하지만, 초기불교에 근거한 부처님은 없습니다. 대부분의 종교가 그렇듯이, 시간이 흐르며 불교 또한 다양하게 발전하였습니다. 저는 그 중에서도 '**초기불교**' 즉, '부처님의 살아생전의 말씀을 담은 '니까야 경전'에 담긴 내용을 근거로한 불교'에 관심이 많습니다. 

그래서 좀 더 맞춤 프로폼트를 통해서 초기불교 AI부처님을 만들어봐야겠다고 생각했습니다.

결과적으로는, 초기불교 AI부처님의 대답이 꽤 만족스럽습니다.

## 1. Install

### prerequisite
> * python3
> * streamlit
> * 구글 클라우드 앱엔진 사용을 위한 gcloud CLI, SDK
> * google.cloud.secretmanager

```
#구글 클라우드 sdk 설치
https://cloud.google.com/appengine/docs/flexible/setting-up-environment?tab=python&hl=ko

#라이브러리 설치


pip install streamlit
pip install google-cloud-secret-manager


# local DB 세팅
docker-compose up -d db
flask init-db  # create SQL로 DB 세팅
```
