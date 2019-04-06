import sys
from .common import *

try:
    print("Trying import local.py settings...", file=sys.stderr)
    from .local import *
except ImportError:
    print("Only standart settings...", file=sys.stderr)
