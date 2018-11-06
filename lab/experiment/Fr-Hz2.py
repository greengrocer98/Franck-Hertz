# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.backends.backend_pgf import FigureCanvasPgf
mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)
pgf_with_latex = {
    "pgf.texsystem": "xelatex",         # use Xelatex which is TTF font aware
}

mpl.rcParams.update(pgf_with_latex)
plt.rc('text', usetex=True)
plt.rc('font', family='serif', serif = 'CMU Serif', size = 12)
plt.rcParams['text.latex.preamble'] = [
            r'\usepackage{amssymb}',
            r'\usepackage{amsmath}',
            r'\usepackage{amsfonts}',
            r'\usepackage{graphicx}',
            r'\usepackage[english,russian]{babel}',
            r'\usepackage[utf8x]{inputenc}',
            r'\usepackage[T1]{fontenc}',
            ]

data = np.genfromtxt('FrHz2exp.csv', delimiter=';')
exp = np.loadtxt('Fr-Hz2.csv', delimiter=';',skiprows=1,usecols=(0,1,3,4,6,7))
data2 = np.genfromtxt('FrHz2expapprox.csv', delimiter=';')
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.errorbar(exp[:,0]/2,exp[:,1]/10,xerr=.5,yerr=.1,fmt='.',color='#FF7800',label=r'$\varphi_z =40 V$')
ax.plot(data[0,:]/4,data[1,:]/1000,color='#000000')
ax.plot(data2[0,:]/2,data2[1,:]/10,color='#FF00FF')
ax.errorbar(exp[:,2]/2,exp[:,3]/10,xerr=.5,yerr=.1,fmt='.',color='#133CAC',label=r'$\varphi_z =45 V$')
ax.errorbar(exp[:,4]/2,exp[:,5]/10,xerr=.5,yerr=.1,fmt='.',color='#00C618',label=r'$\varphi_z =50 V$')

ax.set_ylabel(r'$i_a, mA$')
ax.set_xlabel(r'$\varphi_y, V$')
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
ax.grid()
ax.legend()
plt.savefig('Fr-Hz2.pdf')