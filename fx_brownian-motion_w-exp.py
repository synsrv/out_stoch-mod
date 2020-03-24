
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


def powerlaw_func_s(t, gamma, s):
    return (t/s+1)**(-1*gamma)


def synsrv_trace_figure(fit=True):

    fig, ax = pl.subplots()
    fig.set_size_inches(5.2*0.5,3*0.5)

    bin_w = 1

    # dpath = "./data/tmp/200302_161015_test_up_cap/data/0000"
    dpath = "./data/tmp/200303_141243_test_up_cap/data/0000"

    with open(dpath+'/namespace.p', 'rb') as pfile:
        nsp=pickle.load(pfile)

    with open(dpath+'/lts.p', 'rb') as pfile:
        lts_df=np.array(pickle.load(pfile))

    # discard synapses present at beginning
    lts_df = lts_df[lts_df[:,1]>0]

    # only take synapses grown in first half of simulation
    t_split = nsp['Nsteps']/2
    lts_df = lts_df[lts_df[:,3]<t_split]

    if len(lts_df)>0:
    
        lts = lts_df[:,2] - lts_df[:,3]

        assert np.min(lts) > 0

        lts[lts>t_split]=t_split

        bins = np.arange(1,t_split+bin_w,bin_w)

        counts, edges = np.histogram(lts,
                                     bins=bins,
                                     density=False)

        srv = 1. - np.cumsum(counts)/float(np.sum(counts))
        centers = (edges[:-1] + edges[1:])/2.

        # label = str(nsp['bn_sig'])+ ', ' + str(nsp['up_cap'])
        # label = r'$P_{\mathrm{prune}} = ' + '%.2f' %(nsp['p_prune']) + '$'
        label = ''



        if fit:

            prm, prm_cov = optimize.curve_fit(powerlaw_func_s,
                                              centers, srv, 
                                              p0=[0.5, 0.5])

            xs = np.arange(1,np.max(centers)+1,0.1)

            bl, = ax.plot([0]+list(xs), 
                          powerlaw_func_s([0]+list(xs),*prm),
                          linestyle='-',
                          color='#2c7fb8',
                          label='$\gamma = %.3f$' % prm[0])
                          # label='$\gamma = %.3f$,\n $s=%.3f$' %(prm[0],
                          #                                       prm[1]))

            ax.plot(xs, (1-29.2/10000)**xs, color='gray', alpha=0.5,
                    lw=2.5, label='exponential')

        ax.plot([0]+list(centers), [1.0]+list(srv),
                '.', label=label,
                markersize=10, markeredgewidth=0.5,
                markerfacecolor='None', color='#2c7fb8')


    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    ax.set_ylim(bottom=5*10**-3)

    ax.set_xlabel('simulation steps')
    ax.set_ylabel('survival probability')

    ax.legend(frameon=False, loc='lower left',
                  prop={'size': 9})

    ax.set_xscale('log')
    ax.set_yscale('log')

    fname = os.path.splitext(os.path.basename(__file__))[0]
    fig.savefig("{}_loglog.pdf".format(fname), dpi=300, bbox_inches='tight')

    ax.set_xscale('linear')
    ax.set_yscale('linear')

    ax.get_legend().remove()

    ax.set_xlim(left=-3, right=100)
    
    fname = os.path.splitext(os.path.basename(__file__))[0]
    fig.savefig("{}_linear.pdf".format(fname), dpi=300, bbox_inches='tight')


    
    

if __name__ == "__main__":

    synsrv_trace_figure(fit=True)
