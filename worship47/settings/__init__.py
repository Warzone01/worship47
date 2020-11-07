# -*- coding: utf-8  -*-
from __future__ import absolute_import, print_function

import os
import sys

#from .celery import *

print("Trying import local.py settings...", file=sys.stderr)
from .local import *
