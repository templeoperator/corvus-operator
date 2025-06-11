#!/usr/bin/env python3
import time
with open('/var/log/temple/mirror_log.json', 'a') as log:
    for i in range(10):
        log.write('{"payload":"CORVUS AUTONOMOUS: REMOTE LOGIC %d"}\\n' % i)
        log.flush()
        time.sleep(10)
