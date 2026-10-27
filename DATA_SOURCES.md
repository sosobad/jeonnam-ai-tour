# 데이터와 사진 출처

확인일: **2026-10-27**. 수록 범위는 전라남도 여수·담양·목포의 12곳입니다. 전남 전체를 포괄하는 관광 DB가 아닌 MVP 표본입니다.

## 관광정보

지자체 관광 포털과 한국관광공사 관광 기사에서 관광지의 명칭·지역·대표 특성을 확인하고 직접 짧게 요약했습니다. 원문의 긴 설명·사진을 무단 전재하지 않습니다. 주소는 길찾기용 상세 주소가 아닌 소재 일대이며 여행 팁과 테마는 이 프로젝트의 편집 정보입니다. 요금·운영시간·연락처·좌표는 검증하지 않아 제공하지 않습니다.

- 여수: [오동도 공식 안내](https://yeosu.go.kr/tour/travel/10tour/odongdo), [여수관광 포털](https://yscms.yeosu.go.kr/tour?main=true), [여수 테마별 추천코스](https://www.yeosu.go.kr/tour/my_tour/re_course/recommend_course).
- 담양: [담양군 관광 안내 연결 포털](https://www.damyang.go.kr/index.damyang?menuCd=DOM_000000103001000000), [한국관광공사 담양 여행기사](https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=cdedf0c6-f90e-4108-83a1-f4b2fe8db30a).
- 목포: [목포시 유달산 안내](https://munhak.mokpo.go.kr/tour/attraction/nineplace/yudalsan), [목포문화관광](https://www.mokpo.go.kr/tour), [목포 등산·둘레길 안내](https://tour.mokpo.go.kr/tour/theme/climb).

관광지별 링크는 아래 목록과 `data/attractions.csv`의 `source_url`에 보관합니다. 포털 링크는 개별 명소 상세 페이지가 아닌 경우가 있습니다. 링크 내용과 운영 상태는 이후 변경될 수 있습니다.

## 사진 이용 조건

사진은 Wikimedia Commons API의 파일 설명·저작자·라이선스 메타데이터를 조회해 재사용 가능한 파일만 수집했습니다. 각 파일을 최대 1000×800 범위로 축소하고 JPEG로 변환했습니다. 원본 라이선스를 유지하며 저작자·원본 파일·라이선스를 앱과 이 문서에 표시합니다. CC BY-SA 사진의 변형본은 같은 라이선스 조건을 따릅니다. Public domain/CC0 사진의 크레딧도 추적 가능하도록 남깁니다. 코드와 사진의 이용 조건은 별개입니다.

원본 설명에 포함된 저작자 HTML은 텍스트로 변환했으며, 원래 메타데이터는 `data/image_metadata.json`에 보관합니다. 사진은 수집 시점의 과거 장면으로 현재 현황을 보장하지 않습니다. 향일암은 경내 용 조형물, 삼학도는 항구축제 당시 풍경 사진입니다.

`tools/prepare_data.py`는 사진 수집을 재현하기 위한 도구이며 앱 실행 시 호출하지 않습니다. 재실행하면 검색 결과가 달라질 수 있어 사진과 문서를 다시 검토해야 합니다.

## CSV 열

| 열 | 의미 |
| --- | --- |
| id | MVP 내부 고유 ID |
| region, name | 시·군과 관광지명 |
| description | 출처 기반 편집 요약 |
| tags | 편집 테마, `\|` 구분 |
| address | 탐색용 소재 일대 |
| visit_tip | 편집 여행 팁 |
| source_url | 관광정보 근거 링크 |
| image_path | 저장소 내 사진 파일 |
| image_source_url | Commons 원본 설명 페이지 |
| image_author | 저작자 크레딧 |
| image_license, image_license_url | 사진 이용허락과 전문 링크 |
| verified_date | 출처·사진 메타데이터 확인일, 영업정보 갱신일 아님 |

## 관광지별 정보·사진 크레딧

<!-- GENERATED_CREDITS -->

### JN01 오동도 (여수)

- ????: https://yeosu.go.kr/tour/travel/10tour/odongdo
- ??: [data/images/01.jpg](https://commons.wikimedia.org/wiki/File:Yeosu_Odongdo_20180929_002.jpg)
- ???: Mobius6
- ????: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)
- ??: ?? ???JPEG ??

### JN02 향일암 (여수)

- ????: https://yscms.yeosu.go.kr/tour?main=true
- ??: [data/images/02.jpg](https://commons.wikimedia.org/wiki/File:Dragon_in_Hyangiram.jpg)
- ???: Smiley.toerist
- ????: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)
- ??: ?? ???JPEG ??

### JN03 진남관 (여수)

- ????: https://yscms.yeosu.go.kr/tour?main=true
- ??: [data/images/03.jpg](https://commons.wikimedia.org/wiki/File:%EC%97%AC%EC%88%98%EC%A7%84%EB%82%A8%EA%B4%80.jpg)
- ???: Unknown authorUnknown author
- ????: [Public domain](https://commons.wikimedia.org/wiki/Commons:Licensing)
- ??: ?? ???JPEG ??

### JN04 돌산대교 (여수)

- ????: https://www.yeosu.go.kr/tour/my_tour/re_course/recommend_course
- ??: [data/images/04.jpg](https://commons.wikimedia.org/wiki/File:Dolsan_Bridge2.jpg)
- ???: pcamp
- ????: [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)
- ??: ?? ???JPEG ??

### JN05 죽녹원 (담양)

- ????: https://www.damyang.go.kr/index.damyang?menuCd=DOM_000000103001000000
- ??: [data/images/05.jpg](https://commons.wikimedia.org/wiki/File:Damyang_Jungnogwon_(3).jpg)
- ???: Christian Bolz (크리스티안 볼츠)
- ????: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)
- ??: ?? ???JPEG ??

### JN06 메타세쿼이아길 (담양)

- ????: https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=cdedf0c6-f90e-4108-83a1-f4b2fe8db30a
- ??: [data/images/06.jpg](https://commons.wikimedia.org/wiki/File:Damyang_Metasequoia_Road_2.JPG)
- ???: hyolee2
- ????: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)
- ??: ?? ???JPEG ??

### JN07 관방제림 (담양)

- ????: https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=cdedf0c6-f90e-4108-83a1-f4b2fe8db30a
- ??: [data/images/07.jpg](https://commons.wikimedia.org/wiki/File:%EA%B4%80%EB%B0%A9%EC%A0%9C%EB%A6%BC.JPG)
- ???: Dalgial
- ????: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)
- ??: ?? ???JPEG ??

### JN08 소쇄원 (담양)

- ????: https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=cdedf0c6-f90e-4108-83a1-f4b2fe8db30a
- ??: [data/images/08.jpg](https://commons.wikimedia.org/wiki/File:Soswaewon_1.jpg)
- ???: Kim Dae Jeung
- ????: [CC0](http://creativecommons.org/publicdomain/zero/1.0/deed.en)
- ??: ?? ???JPEG ??

### JN09 유달산 (목포)

- ????: https://munhak.mokpo.go.kr/tour/attraction/nineplace/yudalsan
- ??: [data/images/09.jpg](https://commons.wikimedia.org/wiki/File:Yudalsan_20180415_171946.jpg)
- ???: Matt872000

 This photo was taken with Nikon D5300
- ????: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)
- ??: ?? ???JPEG ??

### JN10 갓바위 (목포)

- ????: https://www.mokpo.go.kr/tour
- ??: [data/images/10.jpg](https://commons.wikimedia.org/wiki/File:Korea-Mokpo_Gatbawi_11-01716.JPG)
- ???: Steve46814
- ????: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)
- ??: ?? ???JPEG ??

### JN11 삼학도 (목포)

- ????: https://tour.mokpo.go.kr/tour/theme/climb
- ??: [data/images/11.jpg](https://commons.wikimedia.org/wiki/File:Mokpo_Harbour_festival_Samhakdo_in_2015_(3).jpg)
- ???: Mar del Este

 This photo was taken with Samsung Galaxy S4
- ????: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)
- ??: ?? ???JPEG ??

### JN12 노적봉 (목포)

- ????: https://munhak.mokpo.go.kr/tour/attraction/nineplace/yudalsan
- ??: [data/images/12.jpg](https://commons.wikimedia.org/wiki/File:Yudalsan_Mokpo_Nojeokbong_peak.jpg)
- ???: Mar del Este
- ????: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)
- ??: ?? ???JPEG ??

