import time
from datetime import datetime
import re
from typing import Dict, Tuple

from flask import Flask, request, jsonify
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('database.json')


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.json
    found, template = find_template(data)
    if found:
        return jsonify({'form_name': template['name']})
    else:
        return jsonify(template)


def find_template(data: Dict[str, str]) -> Tuple[bool, Dict[str, str]]:
    data_fields = set(data.keys())

    """
    По скольку из скрипта запросы поступают очень быстро, может случиться так, что db.all() будет вызван в тот
    момент, когда файл database.json будет открыт другим запросом и будет ошибка. Поэтому просто пробуем 
    взять данные после небольшой задержки
    """
    while 1:
        try:
            all_records = db.all()
            break
        except ValueError:
            time.sleep(0.5)

    for template in all_records:
        template_fields = set(template.keys()) - {'name'}

        if template_fields.issubset(data_fields):
            found = all(validate(data[field]) == template[field] for field in template_fields)
            if found:
                return found, template

    for field in data_fields:
        data[field] = validate(data[field])

    return False, data


def validate(value: str) -> str:

    if is_email(value):
        return 'email'

    elif is_phone(value):
        return 'phone'

    elif is_date(value):
        return 'date'

    return 'text'


def is_date(value: str) -> bool:
    date_formats = ['%d.%m.%Y', '%Y-%m-%d']
    for format_ in date_formats:
        try:
            datetime.strptime(value, format_)
            return True
        except ValueError:
            pass
    return False


def is_phone(value: str) -> bool:
    pattern = re.compile(r"^\+7 \d{3} \d{3} \d{2} \d{2}$")
    return bool(pattern.match(value))


def is_email(value: str) -> bool:
    pattern = re.compile(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return bool(pattern.match(value))


if __name__ == '__main__':
    app.run(debug=True)
