#!/usr/bin/env python

import os
import sys
import shutil
import subprocess

ipynbf = sys.argv[1]

cur_dir = os.path.dirname(os.path.realpath(__file__))
doc_dir = os.path.join(cur_dir, 'templates')
tmp_dir = os.path.join(cur_dir, 'tmp')

if os.path.exists(tmp_dir):
    shutil.rmtree(tmp_dir)

shutil.copytree(doc_dir, tmp_dir)
shutil.copy(ipynbf, tmp_dir)

os.chdir(tmp_dir)
try:
    subprocess.check_call('ipython nbconvert {} --to slides --post serve '\
                          '--config slides_config.py'.format(ipynbf), shell=True)
finally:
    os.chdir(cur_dir)
    shutil.rmtree(tmp_dir)

