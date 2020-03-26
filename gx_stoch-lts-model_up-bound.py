
import matplotlib
matplotlib.use('Agg')

from matplotlib import style
style.use('classic')

import matplotlib.pyplot as pl
from matplotlib import rc

matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath',
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}'
]  

import argparse, sys, os, itertools, pickle
import numpy as np
from scipy import optimize


def bm_upbound_figure():

    fig, ax = pl.subplots()
    fig.set_size_inches(6./2,1.5)

    dpath = "./data/brownian-motion/" +\
            "200326_145800_brownian-motion_traces-with-up-cap/" +\
            "data/0000"

    with open(dpath+'/namespace.p', 'rb') as pfile:
        nsp=pickle.load(pfile)

    with open(dpath+'/xt.p', 'rb') as pfile:
        xt=np.array(pickle.load(pfile))


    idx = 15
    # xlow, xhigh = 15, nsp['Nsteps']-1
    xlow, xhigh = 5, 925
    up_cap_high = nsp['up_cap']*1.4

    sep = np.where(xt[:,idx]==nsp['X_0'])[0]
    # for x in sep:
    #     ax.axvline(x)

    # ax.plot(range(xlow, sep[0]), xt[xlow:sep[0],idx],
    #         color='grey', alpha=0.7)
    # ax.plot(range(sep[0], sep[1]), xt[sep[0]:sep[1],idx],
    #         color='grey', alpha=0.7)
    ax.plot(range(sep[1], sep[2]), xt[sep[1]:sep[2],idx],
            color='grey', alpha=0.7)

    # I'm skipping a few values here purely for visualization purposes
    # exact values are not important here as this grophic only explains
    # the model and does not present results
    ax.plot(range(sep[2]+3, sep[3]), xt[sep[2]+3:sep[3],idx], color='black')

    # skipping some values here as well, same reasoning as above
    ax.plot(range(sep[3]+3, xhigh), xt[sep[3]+3:xhigh,idx],
            color='grey', alpha=0.7)
    

    # upper boundaries    
    ax.plot([xlow,xhigh],[nsp['up_cap']]*2, color='black')

    ax.plot([xlow,xhigh],[up_cap_high]*2, '--', color='black')


    ax.set_xlim(left=xlow-15, right=xhigh)
    ax.set_ylim(bottom=-0.0875)
   
    pl.xticks([xlow, sep[2], sep[3], xhigh],
              ['$t=0$', '', '', '$t=t_{\mathrm{max}}$'])
    
    pl.yticks([nsp["X_0"], nsp["up_cap"], up_cap_high],
              ["$X_{\mathrm{insert}}$", "$\Theta_1$", "$\Theta_2$"])

    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    pl.yticks([nsp["X_prune"], xt[xhigh,idx]],
              ["$X_\mathrm{prune}$", "$X(t_{\mathrm{max}})$"])

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    ax.tick_params(axis='x', which='major', pad=7)

    z,k = sep[2], sep[3]
    
    l = k-z
    mid = z+(k-z)/2
    sep = 30
    hl=(k-z)*0.025
    hw=0.03

    ax.arrow(mid-sep,-0.35, -(l/2-sep), 0., clip_on=False, shape='full',
             head_width=hw, head_length=hl,
             head_starts_at_zero=False, color='k',
             length_includes_head=True)

    ax.arrow(mid+sep,-0.35, (l/2-sep), 0., clip_on=False, shape='full',
             head_width=hw, head_length=hl,
             head_starts_at_zero=False, color='k',
             length_includes_head=True)

    ax.text(mid, -0.38, '$T$', fontdict={'ha': 'center'}, clip_on=False)


    fname = os.path.splitext(os.path.basename(__file__))[0]
    fig.savefig("{}".format(fname)+'.pdf', dpi=300,
                bbox_inches='tight')




if __name__ == "__main__":

    bm_upbound_figure()
    
