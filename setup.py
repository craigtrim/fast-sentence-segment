# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fast_sentence_segment',
 'fast_sentence_segment.bp',
 'fast_sentence_segment.dmo',
 'fast_sentence_segment.svc']

package_data = \
{'': ['*']}

install_requires = \
['baseblock', 'spacy==3.3']

setup_kwargs = {
    'name': 'fast-sentence-segment',
    'version': '0.1.4',
    'description': 'Fast and Efficient Sentence Segmentation',
    'long_description': "# Fast Sentence Segmentation (fast-sentence-segment)\nFast and Efficient Sentence Segmentation\n\nUsage\n```python\nfrom fast_sentence_segment import segment_text\n\nresults = segment_text(\n    'here is a dr. who says something.  and then again, what else?  i dont know.  Do you?')\n\nassert results == [\n    [\n        'here is a dr. who says something.',\n        'and then again, what else?',\n        'i dont know.',\n        'Do you?'\n    ]\n]\n```\n\nWhy use a double-scripted list?\n\nThe segementation process will segment into paragraphs and sentences.  A paragraph is composed of 1..* sentences, hence each list of lists is equivalent to a paragraph.\n\nThis usage\n```python\nresults = segment_text(input_text, flatten=True)\n```\nWill return a list of strings, regardless of paragraph delimitation.\n",
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': 'Craig Trim',
    'maintainer_email': 'craigtrim@gmail.com',
    'url': 'https://github.com/craigtrim/fast-sentence-segment',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
