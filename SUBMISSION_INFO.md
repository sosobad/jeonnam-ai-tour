# 전남 여행 미니프로젝트 제출 정보

## 1. 프로젝트 개요

- **프로젝트명:** 나만의 전남 여행 플래너
- **개발 환경:** VS Code, Python 3.12, Streamlit, pandas
- **개발 방식:** Codex를 활용한 바이브 코딩
- **데이터 범위:** 전라남도 여수·담양·목포 관광지 총 12곳 (지역별 4곳)

**주요 기능**
- 지역별 관광지 검색 및 필터
- 관광지 사진과 상세정보 제공
- 여행 기간과 취향에 따른 맞춤형 여행 코스 추천
- 지역별 관광지 수 시각화
- OpenAI API를 활용한 추가 AI 여행 추천

**추천 방식:** 기본 추천은 관광지 데이터와 여행 취향을 활용한 규칙 기반 추천이며, OpenAI API를 통한 AI 추천 기능을 선택적으로 제공합니다.

## 2. GitHub 소스 코드

- **GitHub URL:** https://github.com/sosobad/jeonnam-ai-tour
- **저장소:** jeonnam-ai-tour
- **브랜치:** main

## 3. Streamlit Community Cloud 배포

- **배포 URL:** https://jeonnam-trip-planner.streamlit.app/
- **배포 플랫폼:** Streamlit Community Cloud
- **실행 파일:** `app.py`
- **의존성 파일:** `requirements.txt`

GitHub 저장소의 소스 코드를 Streamlit Community Cloud에 연결하여 웹앱을 배포했습니다.

OpenAI API 키는 보안을 위해 Streamlit Cloud의 Secrets에 별도로 설정합니다.

## 4. 데이터 및 관광지 이미지 출처

**관광정보 출처**
- 여수시 관광 안내: https://www.yeosu.go.kr/tour
- 담양군 관광 안내: https://www.damyang.go.kr/
- 목포시 관광 안내: https://www.mokpo.go.kr/tour
- 한국관광공사 대한민국 구석구석: https://korean.visitkorea.or.kr/

**관광지 사진 출처**
- Wikimedia Commons: https://commons.wikimedia.org/

사진은 CC BY, CC BY-SA, CC0 및 Public Domain 라이선스 자료를 사용했습니다.

관광지별 원본 URL, 사진 저작자, 라이선스 및 상세 출처는 프로젝트의 `DATA_SOURCES.md` 파일에 정리했습니다.

- **자료 확인일:** 2026년 10월 27일
- **관광지 수:** 총 12곳
- **대상 지역:** 여수 4곳, 담양 4곳, 목포 4곳

관광지 설명과 여행 팁은 참고 자료를 바탕으로 정리했으며, 운영시간·요금·실제 이동 경로를 실시간으로 제공하지는 않습니다.

## 5. 실행 방법

프로젝트 최상위 폴더에서 다음 명령어를 실행합니다.

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

실행 후 브라우저에서 `http://localhost:8501`로 접속합니다.

OpenAI API 키가 없어도 기본 관광지 검색과 규칙 기반 여행 추천 기능을 사용할 수 있습니다.

## 6. 프로젝트 구현 내용

- 전남 관광지 12곳의 이미지 및 상세정보 구성
- 관광지 검색과 지역별 필터 기능 구현
- 여행 취향 및 기간에 따른 추천 알고리즘 구현
- OpenAI API를 활용한 추가 여행 코스 추천 기능 구현
- pandas 기반 관광지 데이터 처리 및 시각화
- GitHub 소스 코드 관리
- Streamlit Community Cloud 웹앱 배포

## 7. 제출 자료

**소스 코드**

https://github.com/sosobad/jeonnam-ai-tour

**웹앱 배포 주소**

https://jeonnam-trip-planner.streamlit.app/

**데이터 및 사진 출처**

프로젝트 저장소의 `DATA_SOURCES.md` 참고

---

**프로젝트명:** 나만의 전남 여행 플래너

**제출일:** 2026년 10월 27일
