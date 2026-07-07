# CareerFit AI Design Skill

## 목적

CareerFit AI React UI를 취업·공모전 데이터 기반 AI 포트폴리오 코치처럼 보이게 만든다.

## 디자인 목표

- 신뢰감 있는 AI 코치 서비스
- 발표 화면에서 한눈에 이해되는 구조
- 입력, 분석 결과, 출처, 신뢰도가 분리된 화면
- 과도하게 화려하기보다 설명 가능한 디자인

## 화면 구조

1. Header
  - 서비스명: CareerFit AI
  - 한 줄 설명: 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치
2. InputForm
  - 전공 입력
  - 보유 스킬 입력
  - 관심 직무 입력
  - 분석 버튼
3. ResultCard
  - answer
  - matched_skills
  - missing_skills
  - recommended_projects
  - confidence
4. SourceCard
  - sources 목록
  - title
  - type
  - matched_reason

## 색상 규칙

- 기본 색상: blue, slate
- 배경: 밝고 단순하게
- 강조: matched_skills, confidence, sources
- 경고: error 상태는 red 계열
- low confidence는 yellow 또는 amber 계열



## UI 상태

반드시 구분해야 하는 상태:

- empty: 아직 분석 전
- loading: 분석 요청 중
- success: 결과 표시
- error: 요청 실패
- no sources: sources가 비어 있음



## 컬러 팔레트

- primary: #3B82F6 (파란색 — 신뢰, 전문성)
- secondary: #10B981 (초록색 — 성장, 추천)
- background: #F8FAFC (연한 회색)
- text-primary: #1E293B
- text-muted: #64748B
- border: #E2E8F0
- error: #EF4444
-  primary: "#2563EB", // 핵심 버튼, 주요 강조 색상
-  secondary: "#38BDF8", // 보조 강조, 태그, 아이콘
-  background: "#F8FAFC", // 전체 배경
-  surface: "#FFFFFF", // 카드, 입력창 배경
-  text: "#111827", // 기본 본문 텍스트
-  muted: "#6B7280", // 설명 텍스트, 보조 정보
-  border: "#E5E7EB", // 카드/입력창 테두리
-  error: "#EF4444" // 오류 메시지



## 타이포그래피

### 제목

- 페이지 제목: `text-3xl font-bold text-gray-900`
- 섹션 제목: `text-xl font-semibold text-gray-900`
- 카드 제목: `text-lg font-semibold text-gray-900`

### 본문

- 기본 본문: `text-base text-gray-700 leading-relaxed`
- 설명 문구: `text-sm text-gray-500`
- 태그/라벨: `text-xs font-medium`

### 규칙

- 제목은 짧고 명확하게 작성한다.
- 본문은 한 문단을 너무 길게 만들지 않는다.
- 대학생 사용자가 이해하기 쉽게 전문 용어는 짧게 설명한다.
- 중요한 키워드는 `font-semibold` 정도로만 강조한다.

## 컴포넌트 구조

- App.jsx: 최상위, 상태 관리, API 요청
- InputForm.jsx: 전공·스킬·직무 입력 폼
- ResultCard.jsx: AI 분석 답변 출력 (초록 왼쪽 테두리)
- SourceCard.jsx: 출처 공고 목록 출력



## 레이아웃 규칙

- 최대 너비: max-w-2xl mx-auto
- 카드 내부 여백: p-6
- 컴포넌트 간격: gap-4 / space-y-4
- 모서리: rounded-xl (카드), rounded-lg (버튼)



## 금지 사항

- API Key를 화면에 표시하거나 localStorage에 저장
- 다크 배경에 흰 텍스트 (가독성 우선)
- 아이콘 없이 버튼만 사용 (텍스트 레이블 필수)

이 대화상자를 닫으려면 Escape 키를 누르세요

## 금지

- sources를 숨기지 않는다.
- confidence를 완전히 생략하지 않는다.
- 과도한 애니메이션을 넣지 않는다.
- 실제 없는 채용 정보처럼 보이게 꾸미지 않는다.
- React 코드에 API Key를 넣지 않는다.

- 너무 강한 원색을 많이 사용하지 않는다.
- 검정 배경 기반의 무거운 UI를 사용하지 않는다.
- 카드에 그림자를 과하게 넣지 않는다.
- 한 화면에 너무 많은 정보를 한꺼번에 보여주지 않는다.
- 버튼 색상을 여러 개 섞지 않는다.
- 모든 텍스트를 굵게 처리하지 않는다.
- 대학생 사용자를 어린아이처럼 대하는 문구를 사용하지 않는다.
- 출처 없는 결과를 확정적인 말투로 보여주지 않는다.
- 에러 메시지를 차갑게 작성하지 않는다.

## 발표용 기준

발표자가 화면을 보며 다음을 설명할 수 있어야 한다.

1. 사용자가 무엇을 입력하는가?
2. AI가 어떤 분석 결과를 주는가?
3. 어떤 공고 또는 데이터가 근거인가?
4. 신뢰도가 높거나 낮은 이유는 무엇인가?



