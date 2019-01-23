#!/usr/bin/env python3

import json
from pathlib import Path
from urllib.parse import urlparse, urljoin, urlunparse


def set_default_docs_link(layer):
    if 'docs' in layer:
        return
    repo = layer['repo']
    repo_parsed = urlparse(repo)
    netloc = repo_parsed.netloc
    docs = None
    if netloc == 'github.com':
        docs = urljoin(repo, '#readme')
    elif netloc == 'git.launchpad.net':
        docs = urljoin(repo, 'tree/README.md')
    elif netloc in ('code.launchpad.net', 'launchpad.net'):
        docs = urljoin(
            urlunparse(repo_parsed._replace(netloc='bazaar.launchpad.net')),
            'files/README.md')
    elif netloc == 'bazaar.launchpad.net':
        docs = urljoin(repo, 'files/README.md')
    else:
        docs = repo
    layer['docs'] = docs


readme_file = Path('README.md')
readme = readme_file.read_text().splitlines()

for layer_type in ('layers', 'interfaces'):
    start = readme.index('<!-- list-of-{} -->'.format(layer_type))
    end = readme.index('<!-- /list-of-{} -->'.format(layer_type))
    del readme[start+1:end]
    readme.insert(start+1, '')
    readme.insert(start+2, '| ID | Repo | Docs | Name | Summary |')
    readme.insert(start+3, '| --- | --- | --- | --- | --- |')
    for layer_file in sorted(Path(layer_type).glob('*.json')):
        end = readme.index('<!-- /list-of-{} -->'.format(layer_type))
        layer = json.loads(layer_file.read_text())
        set_default_docs_link(layer)
        readme.insert(end,
                      '| {id} '
                      '| [Repo]({repo}) '
                      '| [Docs]({docs}) '
                      '| {name} '
                      '| {summary} |'.format(**layer))
    readme.insert(end+1, '')

readme_file.write_text(''.join('{}\n'.format(l) for l in readme))
