# -*- coding: utf-8 -*-
from flask import request
from flask.views import MethodView


from app.extensions import mongo
from app.util import bson_to_json, bson_obj_id

from . import *

import json

class ItemAPI(MethodView):
    def get(self, item_id):
        if item_id is not None:
            item = mongo.db['users'].find_one({'_id': bson_obj_id(item_id)})
            return bson_to_json(item)
        else:
            params = {}
            for k, v in request.args.items():
                if v:
                    # params['attributes.'+k] = v.strip()
                    params[k] = v.strip()
            cursor = mongo.db['users'].find(params)
            items = [bson_to_json(item) for item in cursor]
            return json.dumps(items)

    def post(self):
        return 'POST'


    def put(self, item_id):
        return 'PUT'

    def delete(self, item_id):
        return 'DELETE'



item_view = ItemAPI.as_view('item_api')
api.add_url_rule('/items/', defaults={'item_id': None}, view_func=item_view, methods=['GET', ])
api.add_url_rule('/items/', view_func=item_view, methods=['POST', ])
api.add_url_rule('/items/<item_id>', view_func=item_view, methods=['GET', 'PUT', 'DELETE', ])


