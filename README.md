# # CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치

## 프로젝트 개요

```markdown
취업, 공모전을 준비하며, 어떤 스킬을 준비해야 할지, 무엇부터 시작해야 할지, 다른 사람들은 얼마나 준비해서 오는지 감이 잡히지 않아 어려웠다.
CareerFit Ai가 직무별 요구 스킬을 데이터로 정리하고,내 역량과 비교해 부족한 것들을 알려준다. 어떤 지식들이 필요하며 그 지식은 어디서 습득할 수 있는지 찾아주길 바란다.

```

## 기술 스택

| 영역 | 기술 |

|---|---|

| 백엔드 | Python, FastAPI |

| AI API | Gemini 2.5 Flash-Lite |

| 데이터 | Pandas, SQLite, ChromaDB |

| 프론트엔드 | React, Vite |

| 실행 환경 | Docker |

## 진행 현황

- [x] 1일차: 프로젝트 기획 및 개발 환경 세팅

- [x] 2일차: FastAPI 서버 구축 및 Gemini API 연결

- FastAPI 기반 백엔드 환경을 구성하고 Python 개발 환경 세팅을 완료했습니다.
- `/health`, `/jobs`, `/analyze` API 엔드포인트를 구현했습니다.
- Gemini 2.5 Flash-Lite API를 연동하여 AI 응답 기능을 연결했습니다.
- 환경변수를 활용해 API 키 및 설정 정보를 관리하도록 구성했습니다.
- mock mode 환경변수를 추가하여 테스트 환경을 분리할 수 있도록 설정했습니다.

- [x] 3일차: 데이터 파이프라인 구축

- 404 오류, 링크가 안 열리는 오류를 디버깅하였습니다.
- jobs.csv 파일을 추가하였습니다.
- FastAPI에서 Ollama를 연결하였습니다.
- 다양한 함수들을 추가하였습니다.
- RAG용 문서 데이터를 생성하여 AI가 참고할 수 있는 지식 기반을 구축했습니다.

- [x] 4일차: RAG 기반 서비스 + React UI

- Gemini, Mistral(Hugging Face/Llama) 등 다양한 LLM과 연동하여 검색 결과 기반 답변을 생성하도록 구현했습니다.
- React(Vite) 기반 프론트엔드와 FastAPI 백엔드를 연동하여 `/analyze` API를 통해 결과를 출력하도록 구현했습니다.
- UI 컴포넌트를 구현하고 프로젝트 구조를 구성했습니다.
- 프로젝트 실행 방법과 개발 환경을 README에 정리하고 개발 환경(VS Code, Continue 등)을 설정했습니다.

- [x] 5일차: Docker + 포트폴리오 완성

- 서버 실행 및 api 확인 완료하였습니다.
- Docker 환경을 구성하고 Dockerfile을 수정 및 개선하였습니다.
- 최종 커밋을 완료하였습니다.

---



## 실행 방법



### Docker로 실행 (권장)

```bash
docker build -t careerfit-ai ./backend

docker run -p 8000:8000 \
  --env-file backend/.env \
  careerfit-ai
```

API 문서

```
http://localhost:8000/docs
```



### 로컬 실행

```bash
cd backend

source venv/bin/activate
# Windows
# venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

---



## 데이터 파이프라인

```
jobs.csv
    │
    ▼
Pandas 전처리
    │
    ▼
SQLite 저장
    │
    ▼
ChromaDB 벡터 저장
    │
    ▼
RAG 검색
    │
    ▼
Gemini 응답 생성
```

전처리 실행

```bash
python data/preprocess.py
```

---



## 주요 기능

- RAG 기반 취업 공고 검색
- AI 기반 역량 분석 및 맞춤형 피드백
- 참고한 공고(Source) 함께 제공
- SQLite와 ChromaDB를 활용한 검색 시스템
- Docker 기반 실행 환경 지원

---



## 프로젝트 구조

```
careerfit-ai/
├── backend/
│   ├── data/
│   ├── routers/
│   ├── services/
│   ├── main.py
│   └── Dockerfile
├── frontend/
├── README.md
```

---



## 향후 개선

- [ ] 이력서 PDF 업로드 기능
- [ ] 공고 마감일 필터링 및 알림
- [ ] RAG 검색 품질 평가(Ragas)
- [ ] 사용자 맞춤 추천 기능 고도화

---



## 개발 과정

프로젝트를 Docker 환경에서 실행하는 과정에서 ChromaDB 권한 문제와 컨테이너 실행 오류가 발생했습니다. Dockerfile을 개선하고 실행 환경을 수정하여 컨테이너에서 안정적으로 FastAPI 서버와 ChromaDB가 동작하도록 해결했습니다.

---



## Developer

- Name: 정다섬
- Role: Backend / AI Service Development
- GitHub: [https://github.com/lululudaseom/careerfit_ai_new](https://github.com/lululudaseom/careerfit_ai_new)

