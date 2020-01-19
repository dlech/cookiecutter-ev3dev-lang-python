import os
import sys

code = os.system('poetry --version')
if code:
    print("Ensure that poetry is installed and available in the PATH environment variable")

sys.exit(code)
