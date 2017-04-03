import subprocess
import urllib.parse

import requests
from utilities import choose_from

name = 'technote'
tags = ['doc', 'document', 'github']

BROWSER_COMMAND = '/opt/google/chrome/chrome'
SEARCH_URL = 'https://api.github.com/search/code'
WEB_URL = 'https://github.com/YuKitAs/tech-note/blob/master/'


def do(self, line):
    """Search a tech note and show it."""
    line = line.strip()
    if len(line) == 0:
        print('Please specify a keyword.')
    else:
        search_results = __search_for_documents(line)
        if len(search_results) == 0:
            print('No tech note found with keyword "%s"' % line)
        else:
            tech_note_path = choose_from(search_results, 'documents', 'a document', confirm_single_result=False)
            if tech_note_path is not None:
                subprocess.call([BROWSER_COMMAND, urllib.parse.urljoin(WEB_URL, tech_note_path)])


def __search_for_documents(keyword):
    query = '%s extension:md repo:YuKitAs/tech-note' % keyword
    response = requests.get(SEARCH_URL, params={'q': query})
    if response.status_code != 200:
        return []

    results = []
    for item in response.json()['items']:
        results.append(item['path'])

    return results
