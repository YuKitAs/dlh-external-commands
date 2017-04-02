name = 'sayhello'
tags = ['hello', 'hello world', 'example']


def do(self, line):
    """An example of the implementation of an external command."""
    print('Hello %s!' % (line if len(line) != 0 else 'world'))
