"""One-time, attributed Wikimedia Commons asset collection. Not used at app runtime."""
import csv
import html
import json
import re
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
ITEMS = [
    ('여수', '오동도', 'Odongdo', '동백 숲과 바다를 함께 즐기는 섬 산책 명소.', '자연|바다|산책', '여수시 오동도로 일대', '동백 숲 산책로와 해안 풍경을 천천히 감상해 보세요.', 'https://yeosu.go.kr/tour/travel/10tour/odongdo'),
    ('여수', '향일암', 'Hyangiram', '바다를 내려다보는 산사로 해맞이 풍경이 알려져 있습니다.', '역사|바다|사진', '여수시 돌산읍 향일암로 일대', '오르는 길에 계단과 좁은 바위 통로가 있어 편한 신발을 권합니다.', 'https://yscms.yeosu.go.kr/tour?main=true'),
    ('여수', '진남관', 'Jinnamgwan', '여수의 역사와 전통 목조건축을 만나는 문화유산.', '역사|문화|사진', '여수시 동문로 일대', '문화유산 관람 가능 구역은 공식 안내를 확인하세요.', 'https://yscms.yeosu.go.kr/tour?main=true'),
    ('여수', '돌산대교', 'Dolsan Bridge', '여수 도심과 돌산을 잇는 다리로 항구 경관을 감상하기 좋습니다.', '바다|야경|사진', '여수시 돌산대교 일대', '다리는 조망 대상으로 추천하며 도로 위 정차는 피하세요.', 'https://www.yeosu.go.kr/tour/my_tour/re_course/recommend_course'),
    ('담양', '죽녹원', 'Jungnogwon', '대나무 숲길을 걸으며 쉬어 가는 담양의 대표 명소.', '자연|산책|힐링', '담양군 담양읍 죽녹원로 일대', '숲길 산책과 휴식 중심으로 여유 있게 둘러보세요.', 'https://www.damyang.go.kr/index.damyang?menuCd=DOM_000000103001000000'),
    ('담양', '메타세쿼이아길', 'Damyang Metasequoia', '키 큰 가로수가 이어지는 담양의 숲길.', '자연|산책|사진', '담양군 담양읍 메타세쿼이아로 일대', '계절에 따라 달라지는 가로수 풍경을 즐길 수 있습니다.', 'https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=cdedf0c6-f90e-4108-83a1-f4b2fe8db30a'),
    ('담양', '관방제림', 'Gwanbangjerim', '담양천을 따라 오래된 나무가 그늘을 만드는 제방 숲.', '자연|산책|힐링', '담양군 담양읍 관방제림 일대', '죽녹원과 묶어 걷기 좋은 코스입니다.', 'https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=cdedf0c6-f90e-4108-83a1-f4b2fe8db30a'),
    ('담양', '소쇄원', 'Soswaewon', '자연과 어우러진 전통 정원의 공간을 만나는 곳.', '역사|문화|힐링', '담양군 가사문학면 소쇄원길 일대', '읍내 관광지와 떨어져 있으므로 별도 이동 시간을 두세요.', 'https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=cdedf0c6-f90e-4108-83a1-f4b2fe8db30a'),
    ('목포', '유달산', 'Yudalsan', '목포 도심과 다도해 경관을 바라보는 산.', '자연|산책|사진', '목포시 유달로 일대', '등산과 둘레길의 난이도가 다르므로 체력에 맞춰 선택하세요.', 'https://munhak.mokpo.go.kr/tour/attraction/nineplace/yudalsan'),
    ('목포', '갓바위', 'Gatbawi Mokpo', '갓을 쓴 듯한 형태의 해안 바위를 만나는 명소.', '자연|바다|사진', '목포시 갓바위 일대', '해안 보행로 통제와 기상 상황을 확인하세요.', 'https://www.mokpo.go.kr/tour'),
    ('목포', '삼학도', 'Samhakdo', '목포 항구 풍경과 함께 산책할 수 있는 공간.', '바다|산책|힐링', '목포시 삼학로 일대', '항구 주변 산책과 휴식 위주로 구성해 보세요.', 'https://tour.mokpo.go.kr/tour/theme/climb'),
    ('목포', '노적봉', 'Nojeokbong Mokpo', '유달산 주변에서 목포의 역사 이야기를 만나는 바위 명소.', '역사|문화|산책', '목포시 유달산 노적봉 일대', '유달산과 가까워 함께 둘러보기 좋습니다.', 'https://munhak.mokpo.go.kr/tour/attraction/nineplace/yudalsan'),
]


def clean(value):
    return html.unescape(re.sub('<[^>]+>', '', value)).strip()


def main():
    session = requests.Session()
    session.headers['User-Agent'] = 'JeonnamTravelMVP/1.0 (educational; Wikimedia attribution)'
    (ROOT / 'data/images').mkdir(parents=True, exist_ok=True)
    records = []
    metadata = {}
    for index, (region, name, query, description, tags, address, tip, source) in enumerate(ITEMS, 1):
        response = session.get('https://commons.wikimedia.org/w/api.php', params={
            'action': 'query', 'format': 'json', 'generator': 'search',
            'gsrsearch': query + ' filetype:bitmap', 'gsrnamespace': 6,
            'gsrlimit': 5, 'prop': 'imageinfo', 'iiprop': 'url|extmetadata', 'iiurlwidth': 800,
        }, timeout=30)
        response.raise_for_status()
        pages = sorted(response.json().get('query', {}).get('pages', {}).values(), key=lambda p: p['index'])
        chosen = None
        for page in pages:
            info = page['imageinfo'][0]
            meta = info['extmetadata']
            license_name = meta.get('LicenseShortName', {}).get('value', '')
            if license_name.startswith(('CC BY', 'CC0', 'Public domain')):
                chosen = (page, info, meta, license_name)
                break
        if not chosen:
            raise RuntimeError(f'No licensed photo: {name}')
        page, info, meta, license_name = chosen
        image_response = session.get(info.get('thumburl', info['url']), timeout=60)
        image_response.raise_for_status()
        from PIL import Image
        from io import BytesIO
        image = Image.open(BytesIO(image_response.content)).convert('RGB')
        image.thumbnail((1000, 800))
        path = f'data/images/{index:02}.jpg'
        image.save(ROOT / path, quality=85)
        records.append(dict(id=f'JN{index:02}', region=region, name=name, description=description,
                            tags=tags, address=address, visit_tip=tip, source_url=source,
                            image_path=path, image_source_url=info['descriptionurl'],
                            image_author=clean(meta.get('Artist', {}).get('value', 'Wikimedia Commons contributor')),
                            image_license=license_name,
                            image_license_url=meta.get('LicenseUrl', {}).get('value', 'https://commons.wikimedia.org/wiki/Commons:Licensing'),
                            verified_date='2026-10-27'))
        metadata[name] = {'title': page['title'], 'description': clean(meta.get('ImageDescription', {}).get('value', '')), 'metadata': meta}
        print(name, page['title'], license_name, flush=True)
    with (ROOT / 'data/attractions.csv').open('w', encoding='utf-8-sig', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    (ROOT / 'data/image_metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
