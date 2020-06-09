#!/usr/bin/env python
import sys

text_err = \
"""Usage:
    -r: To collect data
    -w: To write results
"""

if sys.argv[1] == "-r":
    import raw_data.collect
elif sys.argv[1] == "-w":
    import model.func
else:
    sys.stderr.write(text_err)
