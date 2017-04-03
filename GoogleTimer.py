import re
import subprocess

name = 'googletimer'
tags = ['timer', 'countdown', 'clock']

BROWSER_COMMAND = 'open'
BASE_URL = 'https://www.google.de/#q=timer+'


def do(self, line):
    """Set a timer using Google Search."""
    line = line.strip()
    time_format = re.compile(r'\d+[HhMmSs]')
    if time_format.match(line):
        subprocess.call([BROWSER_COMMAND, '%s%s' % (BASE_URL, line)])
    else:
        print('Please specify time using pattern: "\d+[HhMmSs]"')
