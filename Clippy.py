#!/usr/bin/env python3
import clipboard
import sys

if sys.stdin.isatty():
    sys.exit()
else:
    inp=sys.stdin.read().strip()
    clipboard.copy(inp)
print(inp)
