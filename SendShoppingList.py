import subprocess

name = 'sendshoppinglist'
tags = ['telegram', 'sendtext']

TELEGRAM_COMMAND = '/opt/tg/bin/telegram-cli'

def do(self, line):
    """Send text file as Telegram message to a user."""
    subprocess.call([TELEGRAM_COMMAND, '-W', '-e', 'send_text %s' % line])
