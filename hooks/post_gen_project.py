import os
import sys

code = os.system('poetry install')
if code:
    sys.exit(code)

os.system('git init')
os.system('git add .')
os.system('git commit -m "Initial commit"')
if os.linesep == '\r\n':
    # needed to work around https://github.com/cookiecutter/cookiecutter/issues/405
    os.system('git rm --cached -r .')
    os.system('git reset --hard')
os.system('code . --new-window --goto main.py')
