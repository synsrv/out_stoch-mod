
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl
from matplotlib import rc

rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',   
    r'\usepackage{sansmath}',  
    r'\sansmath'               
    r'\usepackage{siunitx}',   
    r'\sisetup{detect-all}',   
]  

import argparse, sys, os, itertools, pickle
import numpy as np
from scipy import optimize



def traces_figure():

    fig, ax = pl.subplots()
    fig.set_size_inches(5.2*0.5*2.2,3.*0.5)

    bin_w = 1

    # dpath = "./data/tmp/200302_161015_test_up_cap/data/0000"
    dpath = "./data/tmp/200312_103637_brownian-traces/data/0000"

    with open(dpath+'/namespace.p', 'rb') as pfile:
        nsp=pickle.load(pfile)

    with open(dpath+'/xt.p', 'rb') as pfile:
        xt=np.array(pickle.load(pfile))

    for i in range(10):
        ax.plot(xt[:,i])

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    # ax.set_xlim(left=-3, right=100)
    # ax.set_ylim(bottom=5*10**-3)

    # ax.set_xlabel('simulation steps')
    ax.set_ylabel('spine size')   

    # ax.legend(frameon=False, loc='lower left',
    #               prop={'size': 9})
    
    fig.tight_layout()

    fname = os.path.splitext(os.path.basename(__file__))[0]
    fig.savefig("{}".format(fname), dpi=300, bbox_inches='tight')


    
   
    

if __name__ == "__main__":

    traces_figure()
