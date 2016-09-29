#!/usr/bin/env python
# ^ python2, knuckle-heads...

import os
import sys
import locale
from subprocess import Popen, PIPE
import time

#locale.setlocale(locale.LC_ALL, 'en_US')

if len(sys.argv) < 2:
    count = 4000000
else:
    count = int(sys.argv[1])

env = os.environ.copy()
env['LD_LIBRARY_PATH'] = '..'
env['DYLD_LIBRARY_PATH'] = '..'

def runBenchmark(executableName, msg):
    then = time.time()
    p = Popen(['./'+executableName, str(count)], stdout=PIPE, stderr=PIPE, env=env)
    out, err = p.communicate()
    t = time.time() - then
    sys.stdout.write(out + err)
    if p.returncode != 0:
        print '%s error. returncode: %d stderr: %s' % (executableName, p.returncode, out+err)
        sys.exit(1)

    print('%s %s: parsed %s AMP boxes in %.4f seconds (%s boxes/s)' %
          (executableName, msg, locale.format("%d", count, grouping=True),
           t, locale.format("%d", int(count/t), grouping=True)))

for name, msg in (('bench_parsing',     '(current implementation)'),
                  ('bench_parsing_new', '(in testing - unused)')):
    runBenchmark(name, msg)
    print


def runLocalhostBenchmark():
    serverName = 'async_server'
    serverPort = '22380'
    clientName = 'bench_client'
    hostName   = 'localhost'
    localhostCount = count / 50
    p1 = Popen(['./'+serverName, serverPort], stdout=PIPE, stderr=PIPE, env=env)

    then = time.time()
    p2 = Popen(['./'+clientName, hostName+':'+serverPort, str(localhostCount)], stdout=PIPE, stderr=PIPE, env=env)
    out2, err2 = p2.communicate()
    t = time.time() - then

    p1.kill()
    out1, err1 = p1.communicate()

    if p2.returncode != 0:
        print '%s error. returncode: %d' % (executableName, p2.returncode)
        print clientName, 'stdout:'
        print out2
        print clientName, 'stderr:'
        print err2

        print serverName, 'stdout:'
        print out1
        print serverName, 'stderr:'
        print err1
        sys.exit(1)

    print('%s: Made %s AMP calls (back-to-back in series - over '
          'localhost TCP socket) in %.4f seconds (%s calls/s)' %
          (clientName, locale.format("%d", localhostCount, grouping=True),
           t, locale.format("%d", int(localhostCount/t), grouping=True)))

runLocalhostBenchmark()
