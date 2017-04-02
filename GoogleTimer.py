import re
import subprocess

name = 'googletimer'
tags = ['timer', 'countdown', 'clock']


def do(self, line):
    """Set a timer using Google Search."""
    time_format = re.compile(r'\d+[HhMmSs]')
    if time_format.match(line.strip()):
        subprocess.call('open https://www.google.de/#q=timer+%s' % line, shell=True)
    else:
        print('Please specify time using pattern: "\d+[HhMmSs]"')
