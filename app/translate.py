import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'YA_TRANSLATOR_KEY' not in current_app.config or not current_app.config['YA_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth_key = current_app.config['YA_TRANSLATOR_KEY']
    r = requests.get(
        'https://translate.yandex.net/api/v1.5/tr.json/translate'
        '?key={}&text={}&lang={}-{}'.format(auth_key, text, source_language, dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    jobj = json.loads(r.content.decode('utf-8-sig'))
    return jobj['text'][0]
