#!/usr/bin/env python3

import json
from pathlib import Path

readme_file = Path('README.md')
readme = readme_file.read_text().splitlines()

for layer_type in ('layers', 'interfaces'):
    start = readme.index('<!-- list-of-{} -->'.format(layer_type))
    end = readme.index('<!-- /list-of-{} -->'.format(layer_type))
    del readme[start+1:end]
    readme.insert(start+1, '')
    readme.insert(start+2, '| ID | Name | Summary |')
    readme.insert(start+3, '| --- | --- | --- |')
    for layer_file in sorted(Path(layer_type).glob('*.json')):
        end = readme.index('<!-- /list-of-{} -->'.format(layer_type))
        layer = json.loads(layer_file.read_text())
        readme.insert(
            end, '| [{id}]({repo}) | {name} | {summary} |'.format(**layer))
    readme.insert(end+1, '')

readme_file.write_text(''.join('{}\n'.format(l) for l in readme))
