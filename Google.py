import subprocess
import urllib.parse

name = 'google'
tags = ['search']

BROWSER_COMMAND = 'open'
BASE_URL = 'https://www.google.de/#q='


def do(self, line):
    """Search keywords using Google."""
    subprocess.call([BROWSER_COMMAND, '%s%s' % (BASE_URL, urllib.parse.quote_plus(line))])
