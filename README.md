# 나만의 전남 여행 플래너

Streamlit과 pandas로 만드는 수업용 Python 미니프로젝트입니다. 출처가 확인된 여수·담양·목포 관광지 12곳(각 4곳)을 사용합니다. **API 키 없이 네 가지 핵심 기능이 모두 동작합니다.**

## 핵심 기능

| 기능 | 사용 방법 | 구현 원리 |
| --- | --- | --- |
| 지역별 관광지 검색 | 사이드바에서 지역 선택·검색어 입력 | pandas `isin()`과 `str.contains()`로 행을 걸러냅니다. |
| 사진과 상세정보 | 관광지 카드의 상세정보 펼치기 | CSV의 사진 경로를 `st.image()`로 표시하고 설명·방문 팁·출처를 출력합니다. |
| 기간·취향별 코스 추천 | 기간과 취향 선택 후 코스 추천받기 | 태그 일치 개수로 점수를 매겨 하루 같은 지역 최대 2곳을 배정합니다. |
| 지역별 관광지 수 시각화 | 지역별 관광지 수 탭 확인 | `groupby().size()`로 개수를 세고 `st.bar_chart()`로 그립니다. |

화면은 Streamlit 기본 탭·카드·차트와 `.streamlit/config.toml`의 간단한 색상 설정을 사용합니다. 별도의 CSS나 웹 프레임워크는 없습니다. 예산·인원·이동수단 입력은 수업 범위를 줄이기 위해 제외했습니다.

## 실행 방법

Python 3.12를 권장합니다. 프로젝트 폴더의 PowerShell에서 실행하세요.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

브라우저에서 http://localhost:8501 을 엽니다. 기본 기능은 `.env`나 API 키 설정이 필요하지 않습니다.

## 코드 구조

```text
app.py                    # 핵심 기능과 화면을 함수별로 구현
requirements.txt          # 실행에 필요한 패키지
README.md                 # 실행·코드 설명·발표 예시
DATA_SOURCES.md            # 관광정보 출처와 사진 라이선스
.gitignore                # API 키·가상환경 등을 Git에서 제외
.env.example              # 선택 기능의 환경변수 예시
.streamlit/config.toml    # 간단한 테마와 Cloud 실행 설정
data/attractions.csv      # 관광지 12곳, 태그, 사진 경로, 출처
data/images/              # 출처와 라이선스를 확인한 사진 12장
data/image_metadata.json  # 원본 사진 메타데이터 (보관용)
data/contact_sheet.jpg    # 수집 사진 확인용 모음
tools/prepare_data.py     # 기존 자료 수집 도구 (앱 실행 시 불필요)
tools/verify_mvp.py       # 기본 기능 및 선택 API의 자동 검증
```

기존 관광지 CSV·사진·출처 문서·수집 도구는 유지했습니다. 수업에서는 `app.py`와 CSV를 중심으로 설명하면 됩니다. 자료 수집 도구는 실행할 필요가 없습니다.

| 함수 | 역할 |
| --- | --- |
| `load_attractions()` | CSV를 DataFrame으로 읽고 필수 열을 검사합니다. |
| `filter_attractions()` | 지역과 키워드로 관광지를 검색합니다. |
| `recommend_course()` | 기간과 취향으로 기본 코스를 만듭니다. |
| `course_to_markdown()` | 코스를 읽기 쉬운 글로 바꿉니다. |
| `show_attractions()` | 사진 카드와 상세정보를 표시합니다. |
| `show_planner()` | 추천 입력·결과·다운로드를 표시합니다. |
| `count_by_region()` | 지역별 관광지 개수를 계산합니다. |
| `show_statistics()` | 막대그래프와 집계 표를 표시합니다. |
| `setting()` / `generate_itinerary()` | 선택 기능인 OpenAI 설정과 요청을 담당합니다. |
| `main()` | 데이터 로딩, 사이드바, 세 개 탭을 연결합니다. |

## 작동 원리 쉽게 이해하기

### 1. 데이터 읽기와 검색

`pd.read_csv()`가 CSV를 행과 열로 이루어진 DataFrame으로 바꿉니다. 한 행은 관광지 하나입니다. `region`은 지역, `name`은 이름, `tags`는 취향 비교용 테마입니다. 예를 들어 `자연|바다|산책`은 세 가지 테마를 뜻합니다.

지역을 선택하면 `isin()`으로 해당 지역의 행만 남깁니다. 검색어는 이름·지역·설명·태그에서 찾습니다. `regex=False`로 지정해 괄호 같은 문자도 검색어 그대로 처리합니다. 지역을 비우면 전체를 표시하며 검색 결과가 없으면 안내 문구가 나옵니다.

### 2. 사진과 상세정보

CSV의 `image_path`를 프로젝트 폴더 기준으로 찾아 사진을 표시합니다. 사진은 저장소에 있으므로 앱 실행 중 외부 이미지 API를 호출하지 않습니다. 상세정보에는 소재 일대, 여행 팁, 관광정보 링크, 원본 사진과 저작자·라이선스를 표시합니다. 사진이 없으면 안내와 원본 링크를 제공합니다.

### 3. API 없는 기본 추천

기본 추천은 학습하기 쉬운 **규칙 기반 추천**입니다. AI 모델을 학습하거나 API를 호출하지 않습니다.

1. 사이드바에서 선택한 지역의 관광지를 후보로 가져옵니다. 검색어는 추천에 적용하지 않습니다.
2. 선택한 취향과 각 관광지의 테마가 몇 개 일치하는지 셉니다.
3. 점수 내림차순으로 정렬합니다. 점수가 같으면 CSV의 고유 ID 순서로 정합니다.
4. 가장 높은 점수의 남은 관광지 지역을 오늘의 지역으로 정하고, 그 지역에서 최대 2곳을 고릅니다.
5. 고른 관광지를 후보에서 빼고 다음 날을 만듭니다. 중복 방문은 없습니다.
6. 후보가 부족한 날짜에는 자유시간을 안내합니다.

예를 들어 취향이 `자연, 산책`이면 `자연|바다|산책` 관광지는 2점, `바다|야경|사진` 관광지는 0점입니다. 취향을 선택하지 않거나 일치하는 곳이 없으면 모두 0점으로 ID 순서에 따라 추천합니다. 선택 취향은 우선순위이므로 0점 관광지도 같은 날의 두 번째 장소나 이후 날짜에 포함될 수 있습니다.

같은 지역을 하루에 묶지만 실제 거리·교통편으로 최단 경로를 계산하지는 않습니다. 여행 기간은 1~7일입니다. 출력 결과를 `st.session_state`에 보관하므로 다른 검색을 해도 마지막 코스가 유지됩니다. 입력을 바꿨다면 추천 버튼을 다시 눌러야 결과가 바뀌며, 결과 위에 마지막 추천 조건을 표시합니다.

### 4. 지역별 관광지 수

```python
counts = frame.groupby('region').size().rename('관광지 수').to_frame()
st.bar_chart(counts)
```

`groupby('region')`은 같은 지역끼리 묶고, `size()`는 각 그룹의 행 개수를 셉니다. 현재 데이터는 담양·목포·여수 각 4곳이어서 막대 높이가 같습니다. 차트는 검색과 관계없이 전체 12곳을 집계합니다. **전남 전체의 실제 관광지 수 통계가 아닙니다.**

## 선택 기능: OpenAI 추가 추천

기본 코스를 만든 뒤 OpenAI 코스도 함께 보고 싶을 때만 체크박스를 선택합니다. OpenAI Docs의 [Responses API 공식 안내](https://developers.openai.com/api/docs/guides/text)를 참고한 확장 기능입니다.

로컬에서는 `.env.example`을 `.env`로 복사한 뒤 본인 키를 넣습니다. 기존 `.env`가 있다면 그대로 사용합니다.

```dotenv
OPENAI_API_KEY=본인의_API_키
OPENAI_MODEL=gpt-4.1-mini
```

환경변수 또는 Streamlit Secrets에서 키를 읽습니다. 환경변수가 우선이며 `.env`는 기존 환경변수를 덮어쓰지 않습니다. 키는 소스나 CSV에 저장하지 않습니다. 기본 추천은 키와 무관하게 먼저 만들어집니다. AI 선택 후 키가 없거나 인증·통신 등에 실패하면 안내를 표시하고 기본 코스를 유지합니다. API에는 기간·취향·공개 관광정보만 보내며 `store=False`로 요청합니다.

OpenAI 사용에는 API 계정의 결제·모델 접근 권한이 필요합니다. 공개 앱에서는 배포자에게 API 비용이 발생하며 사용자별 요청 제한은 구현하지 않았습니다. AI는 제공 목록만 사용하도록 지시하지만 별도 구조 검증은 없으므로 결과에 오류가 있을 수 있습니다.

## GitHub와 Streamlit Community Cloud 배포

1. 기존 프로젝트 구조 그대로 GitHub 저장소에 업로드합니다. CSV와 `data/images/`를 반드시 포함하세요.
2. `.env`, `.streamlit/secrets.toml`, 가상환경은 `.gitignore`로 제외합니다.
3. [Streamlit Community Cloud](https://share.streamlit.io/)에서 **Create app**을 선택해 저장소·브랜치를 지정합니다.
4. 진입 파일을 `app.py`, Python을 **3.12**로 설정하고 배포합니다. `requirements.txt`로 패키지를 설치합니다.
5. 키 없이도 네 가지 핵심 기능을 확인할 수 있습니다. OpenAI가 필요한 경우에만 앱의 Secrets에 아래 TOML을 입력합니다.

```toml
OPENAI_API_KEY = "본인의_API_키"
OPENAI_MODEL = "gpt-4.1-mini"
```

참고: [공식 배포 문서](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app), [Secrets 관리](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

## 수업 발표 예시

“CSV에 출처가 확인된 전남 관광지 12곳을 정리하고 pandas로 읽었습니다. Streamlit 사이드바에서 지역과 검색어를 받아 관광지를 필터링했습니다. 사진과 설명은 CSV에 연결해 표시했습니다. 추천은 사용자의 취향과 관광지 태그가 일치하는 개수를 점수로 계산하고 하루 두 곳씩 배정했습니다. 지역별 관광지 개수는 groupby로 집계해 막대그래프로 시각화했습니다. 기본 기능은 API 없이 동작하며 OpenAI는 추가 기능으로 분리했습니다.”

학습 순서는 CSV 읽기 → 지역 검색 → 사진·상세정보 → 추천 점수 계산 → 차트 → 선택 API 순서를 권장합니다.

## 검증과 데이터의 범위

```powershell
python -m py_compile app.py tools/prepare_data.py tools/verify_mvp.py
python tools/verify_mvp.py
```

검증 도구는 실제 유료 API를 호출하지 않습니다. 데이터·사진, 추천 점수와 중복 방지·후보 부족, 지역별 집계, Streamlit 검색·기본 추천·키 없는 선택 추천·API 실패 시 기본 코스 유지, 모의 API 요청을 확인합니다.

2026-10-27에 Python 3.12.9와 Streamlit 1.66.0 환경에서 문법 검사와 위 기능 검증을 통과했습니다. 실제 OpenAI 유료 호출과 Community Cloud 원격 배포는 수행하지 않았습니다.

관광정보와 사진 출처 확인일은 2026-10-27입니다. 주소는 탐색용 일대 표기이며 요금·운영시간·예약·날씨·교통편은 실시간 조회하지 않습니다. 실제 방문 전 각 카드의 공식 안내를 확인하세요. 사진 라이선스와 상세 출처는 `DATA_SOURCES.md`를 참고하세요. 기존 수집 도구를 다시 실행하면 데이터·사진이 덮어써지므로 일상 실행과 배포에는 사용하지 않습니다.

### ? ??? ?? API ??

?? ?? `app.py`? ?? ??? `.env`? ???. Cloud? ? ??? Secrets? ????, Secrets? ?????? ?????. `.env`? `tools/.env`, `.streamlit/secrets.toml`? Git ?? ???? ?? ???? ????.

`python tools/check_openai.py`? ?? API ??? ??? ? ????. ? ??? 1? ?? ?? 1?? ???? API ??? ??? ? ????. ???? ????? ??? ???? ?? ?? ?? ? ?? ??? ?????.
