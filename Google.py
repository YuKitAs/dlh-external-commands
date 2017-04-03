import subprocess
import urllib.parse

name = 'google'
tags = ['search']

BROWSER_COMMAND = 'open'
BASE_URL = 'https://www.google.de/#q='


def do(self, line):
    """Search keywords using Google."""
    query_string = urllib.parse.urlencode(line)
    subprocess.call([BROWSER_COMMAND, '%s%s' % (BASE_URL, query_string)])
