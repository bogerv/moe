# coding: utf-8

from . import user
from flask import jsonify
import json

user_data = [
    {
        'id': 1,
        'name': '张三',
        'age': 23
    },
    {
        'id': 2,
        'name': '李四',
        'age': 24
    }
]


@user.route('/<int:user_id>', methods=['GET', ])
def get(user_id):
    for item in user_data:
        if item['id'] == user_id:
            return jsonify(status='success', user=item)


@user.route('/users', methods=['GET', ])
def users():
    data = {
        'status': 'success',
        'users': user_data
    }
    return json.dumps(data, ensure_ascii=False, indent=1)
