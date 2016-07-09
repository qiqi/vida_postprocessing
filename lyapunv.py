import os
import sys
import time
import shutil
import string
import tempfile
import argparse
from subprocess import *

from numpy import *

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(my_path, '..'))

from fds import *
from fds.checkpoint import *
from fds.cti_restart_io import *

checkpoint = load_last_checkpoint(os.path.join(my_path, 'vida'), 4)
_, _, _, lss, G_lss, g_lss, J_hist, G_dil, g_dil = checkpoint
L = lss.lyapunov_exponents()
print(L)
print(L.mean(0))

v = lss.lyapunov_covariant_vectors()
for i in range(4):
    print(v[i,16])
