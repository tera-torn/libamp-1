#!/usr/bin/env python
# ^ python2, knuckle-heads...

import os
import sys
import locale
from subprocess import Popen, PIPE
import time

#locale.setlocale(locale.LC_ALL, 'en_US')

if len(sys.argv) != 2:
    raise ValueError("Pass number of boxes to parse as first argument.")

count = int(sys.argv[1])

env = os.environ.copy()
env['LD_LIBRARY_PATH'] = '..'
env['DYLD_LIBRARY_PATH'] = '..'

def runBenchmark(executableName):
    then = time.time()
    p = Popen(['./'+executableName, str(count)], stdout=PIPE, stderr=PIPE, env=env)
    out, err = p.communicate()
    t = time.time() - then
    sys.stdout.write(out + err)
    if p.returncode != 0:
        print '%s error. returncode: %d stderr: %s' % (executableName, p.returncode, out+err)
        sys.exit(1)

    print('%s: parsed %s AMP boxes in %.4f seconds (%s boxes/s)' % 
          (executableName, locale.format("%d", count, grouping=True),
           t, locale.format("%d", int(count/t), grouping=True)))

for name in ('bench_parsing', 'bench_parsing_new'):
    runBenchmark(name) 
    print
