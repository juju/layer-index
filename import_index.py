#!/usr/bin/env python3

import json
import requests
from pathlib import Path

BASE_URI = 'http://interfaces.juju.solutions/api/v1'
for layer_type in ('layers', 'interfaces'):
    data = requests.get('/'.join([BASE_URI, layer_type])).json()
    for layer in data:
        layer.pop('_id', None)
        layer.pop('lastmodified', None)
        layer.pop('lastModified', None)
        layer.pop('owner', None)
        layer.pop('version', None)
        dest = Path('{}/{}.json'.format(layer_type, layer['id']))
        dest.write_text(json.dumps(layer, sort_keys=True, indent=2))
