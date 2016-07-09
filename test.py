import os
import sys
import time
import shutil
import pickle
import string
import tempfile
import argparse
import itertools
from subprocess import *

from numpy import *

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(my_path, '..', '..'))
vida_path = os.path.abspath(os.path.join(my_path, '..', 'vida'))

from fds import *
from fds.checkpoint import *
from fds.cti_restart_io import *

lss = pickle.load(open('vidalss.pickle'))
v = lss.lyapunov_covariant_vectors()
