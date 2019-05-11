#!/usr/bin/env python3
import clipboard
import sys

if sys.stdin.isatty():
    sys.exit()
else:
    clipboard.copy(sys.stdin.read().strip())
    
