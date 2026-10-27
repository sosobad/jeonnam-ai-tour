"""실제 1일 코스 생성 점검. 키·응답 본문·오류 원문은 출력하지 않습니다."""
import logging
import sys
from pathlib import Path

logging.disable(logging.CRITICAL)
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main():
    import app
    from openai import APIConnectionError, APIStatusError, AuthenticationError, RateLimitError

    if not app.setting('OPENAI_API_KEY'):
        print('KEY_CONFIGURED=False')
        return 1
    print('KEY_CONFIGURED=True', flush=True)
    try:
        data = app.load_attractions()
        candidates = data[data['region'] == '여수']
        result = app.generate_itinerary(candidates, 1, ['바다'])
        valid = bool(result.strip()) and any(name in result for name in candidates['name'])
        print('LIVE_ITINERARY_OK=' + str(valid))
        return 0 if valid else 1
    except AuthenticationError:
        print('LIVE_ITINERARY_OK=False; REASON=AUTHENTICATION')
    except RateLimitError:
        print('LIVE_ITINERARY_OK=False; REASON=QUOTA_OR_RATE_LIMIT')
    except APIConnectionError:
        print('LIVE_ITINERARY_OK=False; REASON=NETWORK')
    except APIStatusError as error:
        print('LIVE_ITINERARY_OK=False; HTTP_STATUS=' + str(error.status_code))
    except Exception:
        print('LIVE_ITINERARY_OK=False; REASON=INCOMPLETE_OR_CONFIGURATION')
    return 1


if __name__ == '__main__':
    sys.exit(main())
