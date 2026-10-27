"""수업용 플래너의 오프라인 기능 검증. 실제 OpenAI API는 호출하지 않습니다."""
import json
import os
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from PIL import Image
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import app


def main():
    data = app.load_attractions()
    assert len(data) == 12 and data.id.is_unique
    for path in data.image_path:
        with Image.open(ROOT / path) as image:
            image.verify()
    assert len(app.filter_attractions(data, ['여수'], '')) == 4
    assert len(app.filter_attractions(data, [], '갓바위')) == 1
    assert app.filter_attractions(data, [], '[없는장소]').empty
    assert app.count_by_region(data)['관광지 수'].to_dict() == {'담양': 4, '목포': 4, '여수': 4}

    course = app.recommend_course(data, 7, ['자연', '산책'])
    places = [place for day in course for place in day['places']]
    assert len(course) == 7 and len(places) == 12
    assert len({place['id'] for place in places}) == 12
    assert course[-1]['places'] == []
    for day in course:
        assert len(day['places']) <= 2
        assert len({place['region'] for place in day['places']}) <= 1
    assert course[0]['places'][0]['score'] == 2
    sea_course = app.recommend_course(data, 1, ['야경'])
    assert sea_course[0]['places'][0]['name'] == '돌산대교'
    empty_tastes = app.recommend_course(data, 1, [])
    assert empty_tastes[0]['places'][0]['id'] == 'JN01'
    assert app.recommend_course(data.iloc[:0], 1, [])[0]['places'] == []
    assert '자유시간' in app.course_to_markdown(course)

    with patch.dict(os.environ, {'OPENAI_API_KEY': ''}), patch.object(app.st, 'secrets', {'OPENAI_API_KEY': 'test-secrets'}):
        assert app.setting('OPENAI_API_KEY') == 'test-secrets'
    with patch.dict(os.environ, {'OPENAI_API_KEY': 'test-env'}), patch.object(app.st, 'secrets', {'OPENAI_API_KEY': 'test-secrets'}):
        assert app.setting('OPENAI_API_KEY') == 'test-secrets'
    with patch.dict(os.environ, {'OPENAI_API_KEY': 'test-env'}), patch.object(app.st, 'secrets', {}):
        assert app.setting('OPENAI_API_KEY') == 'test-env'
    with patch.dict(os.environ, {'OPENAI_API_KEY': 'test-only'}), patch('openai.OpenAI') as client:
        create = client.return_value.__enter__.return_value.responses.create
        create.return_value = SimpleNamespace(status='completed', output_text='## 1일차\n오동도')
        assert '오동도' in app.generate_itinerary(data[data.region == '여수'], 1, ['바다'])
        sent = create.call_args.kwargs
        payload = json.loads(sent['input'])
        assert sent['store'] is False and len(payload['관광지']) == 4
        assert payload['기간_일'] == 1 and payload['취향'] == ['바다']
        assert 'test-only' not in sent['input']

    test = AppTest.from_file(str(ROOT / 'app.py')).run(timeout=30)
    assert not test.exception, test.exception
    assert '나만의 전남 여행 플래너' in test.title[0].value
    assert len(test.subheader) == 14
    test.sidebar.multiselect[0].set_value(['여수']).run()
    assert len(test.subheader) == 6
    test.sidebar.text_input[0].set_value('없는장소123').run()
    assert any('검색 결과가 없습니다' in item.value for item in test.info)
    test.secrets['OPENAI_API_KEY'] = ''
    with patch.dict(os.environ, {'OPENAI_API_KEY': ''}), patch('openai.OpenAI') as api:
        test.button[0].click().run()
        assert not test.exception
        assert 'basic_course' in test.session_state
        assert '오동도' in test.session_state['basic_course']
        assert '여수' in test.session_state['plan_summary']
        api.assert_not_called()
        test.checkbox[0].set_value(True)
        test.button[0].click().run()
        assert any('API 키가 없어' in item.value for item in test.warning)
        assert 'basic_course' in test.session_state
        api.assert_not_called()
    with patch.dict(os.environ, {'OPENAI_API_KEY': 'test-only'}), patch('openai.OpenAI', side_effect=RuntimeError('mock failure')):
        test.button[0].click().run()
        assert not test.exception
        assert any('가져오지 못했습니다' in item.value for item in test.warning)
        assert 'basic_course' in test.session_state
        assert 'ai_course' not in test.session_state
    print('PASS: data/images; search; preference scores; unique daily courses; regional counts; mocked API; no-key and API-failure fallback UI')


if __name__ == '__main__':
    main()
