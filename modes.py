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

template_file = os.path.join(my_path, 'plot_duz.mcr.template')
template = string.Template(open(template_file).read())
layout_file = os.path.join(my_path, 'vida_wake.lay')

lss = pickle.load(open('vidalss.pickle'))
v = lss.lyapunov_covariant_vectors()
v /= sqrt((v**2).sum(2))[:,:,newaxis]

for imode in range(4):
    for i in range(v.shape[1]):
        print(i)
        baseline = os.path.join(vida_path, 'segment{0:02d}_baseline'.format(i))
        pert_000 = os.path.join(vida_path, 'segment{0:02d}_init_perturb000'.format(i))
        pert_001 = os.path.join(vida_path, 'segment{0:02d}_init_perturb001'.format(i))
        pert_002 = os.path.join(vida_path, 'segment{0:02d}_init_perturb002'.format(i))
        pert_003 = os.path.join(vida_path, 'segment{0:02d}_init_perturb003'.format(i))
        baseline_tec = os.path.join(baseline, 'CUTS', 'xcut0.000400.plt')
        pert_000_tec = os.path.join(pert_000, 'CUTS', 'xcut0.000400.plt')
        pert_001_tec = os.path.join(pert_001, 'CUTS', 'xcut0.000400.plt')
        pert_002_tec = os.path.join(pert_002, 'CUTS', 'xcut0.000400.plt')
        pert_003_tec = os.path.join(pert_003, 'CUTS', 'xcut0.000400.plt')
        png_file = os.path.join(my_path, 'png', 'mode{0}_{1:05d}.png'.format(imode, i))
        if os.path.exists(baseline_tec) and os.path.exists(pert_000_tec):
            mcr = template.substitute(LAYOUT=layout_file,
                                      TECPLOT1=baseline_tec,
                                      TECPLOT2=pert_000_tec, A000=v[imode,i,0],
                                      TECPLOT3=pert_001_tec, A001=v[imode,i,1],
                                      TECPLOT4=pert_002_tec, A002=v[imode,i,2],
                                      TECPLOT5=pert_003_tec, A003=v[imode,i,3],
                                      PNGFILE=png_file, TIMESEG=str(i))
            mcr_file = os.path.join(my_path, 'plot_duz.mcr')
            with open(mcr_file, 'w') as f: f.write(mcr)
            check_call(['tec360', '-mesa', '-b', '-p', mcr_file], stdout=PIPE)
        else:
            print baseline_tec, pert_000_tec
            break
