
import matplotlib
matplotlib.use('Agg')

from matplotlib import style
style.use('classic')

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


def bm_upbound_figure():

    fig, ax = pl.subplots()
    fig.set_size_inches(6./2,1.2)

    bin_w = 1

    dpath = "./data/brownian-motion/" +\
            "200325_152759_brownian-motion_traces-with-up-cap/" +\
            "data/0000"

    with open(dpath+'/namespace.p', 'rb') as pfile:
        nsp=pickle.load(pfile)

    with open(dpath+'/xt.p', 'rb') as pfile:
        xt=np.array(pickle.load(pfile))


    xlow, xhigh = 100, 850


    # i, k = 2,0
    # while k<nsp["Nsteps"]:
    #     if xt[i,k]>0:
    #         break
    #     else:
    #         k+=1
    # z=k
    # low=k
    # while low<nsp["Nsteps"]:
    #     if xt[i,low]>0:
    #         low+=1
    #     else:
    #         break

    # xva = range(k-(nsp["Nsteps"]-900)+22,k)
    # yva = xt[11][900:nsp["Nsteps"]][6:-16]

    ax.plot(range(xlow, xhigh), xt[xlow:xhigh,12])

    ax.plot([xlow,xhigh],[nsp['up_cap']]*2, color='black')

    # ax.plot(xva, yva, 'grey')

    # print(yva)




    # yvals = xt[i][k:low]

    # ax.plot(range(k,low),xt[i][k:low], 'black')


    # ax.plot([xlow,k-(nsp["Nsteps"]-900)+22],[nsp["X_0"]]*2, 'black', linestyle=':')

    # while k<nsp["Nsteps"]:
    #     if xt[i,k]>0:
    #         k+=1
    #     else:
    #         break

    # i, l = 16,0
    # while l<nsp["Nsteps"]:
    #     if xt[i,l]>0:
    #         break
    #     else:
    #         l+=1

    # ax.plot(range(k,nsp["Nsteps"]-125),xt[i][l:l+nsp["Nsteps"]-k-125], 'grey')

    # ax.plot([k, nsp["Nsteps"]-125*1.05],[0]*2, 'black', linestyle=':')


    # ax.plot([xlow, nsp["Nsteps"]-125*1.05],[upper_bound]*2, 'black', linestyle=':')
    # ax.plot([xlow, nsp["Nsteps"]-125*1.05],[upper_bound_2]*2, 'black', linestyle=':')


    # print(len(list(range(k,nsp["Nsteps"]))))
    # print(len(xt[i][l:l+nsp["Nsteps"]-k]))


    # ax.set_xlim(xlow, nsp["Nsteps"]-125*1.05)
    # ax.set_ylim(bottom=-0.0875)


    # pl.xticks([z-(nsp["Nsteps"]-900)+22,z,k, nsp["Nsteps"]-125], ['$t=0$', '','', '$t=t_{\mathrm{max}}$'])
    pl.xticks([xlow, xlow+100, xlow+200, xhigh],
              ['$t=0$', '', '', '$t=t_{\mathrm{max}}$'])
    
    # pl.yticks([nsp["X_0"]], ["$X_{\mathrm{insert}}$"])

    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    # # ax
    # pl.yticks([0, xt[i][l+nsp["Nsteps"]-k]], ["$X_\mathrm{prune}$", "$X(t_{\mathrm{max}})$"])

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    ax.tick_params(axis='x', which='major', pad=7)

    # l = k-z
    # mid = z+(k-z)/2
    # sep = 30
    # hl=(k-z)*0.025
    # hw=0.03

    # ax.arrow(mid-sep,-0.35, -(l/2-sep), 0., clip_on=False, shape='full',
    #          head_width=hw, head_length=hl,
    #          head_starts_at_zero=False, color='k',
    #          length_includes_head=True)

    # ax.arrow(mid+sep,-0.35, (l/2-sep), 0., clip_on=False, shape='full',
    #          head_width=hw, head_length=hl,
    #          head_starts_at_zero=False, color='k',
    #          length_includes_head=True)

    # ax.text(mid, -0.38, '$T$', fontdict={'ha': 'center'}, clip_on=False)


    # ax.arrow(z,-0.35, k-z, 0., clip_on=False, shape='full',
    #          head_width=0.05, head_length=(k-z)*0.05,
    #          head_starts_at_zero=False, color='k')


    fname = os.path.splitext(os.path.basename(__file__))[0]
    fig.savefig("{}".format(fname)+'.pdf', dpi=300,
                bbox_inches='tight')




if __name__ == "__main__":

    bm_upbound_figure()
    
