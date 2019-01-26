#!/usr/bin/env python
import os
import subprocess

pid = os.fork()
if pid == 0:  
    pid2 = os.fork()
    if pid2 != 0:
        subprocess.check_call(('pstree', '-Gp'))
else:
    os.waitpid(pid, 0)
    subprocess.check_call(('ps', 'x'))
    subprocess.check_call(('pstree', '-Gp'))
