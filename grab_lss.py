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

import fds

checkpoint = fds.checkpoint.load_last_checkpoint(vida_path, 4)
pickle.dump(checkpoint.lss, open('vidalss.pickle', 'wb'))
