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
            r'\usepackage{amsmath}',
            r'\usepackage{amsfonts}',
            r'\usepackage{graphicx}',
            r'\usepackage[english,russian]{babel}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[T1]{fontenc}',
            ]

data = np.genfromtxt('FrHz1exp.csv', delimiter=';')
exp = np.loadtxt('Fr-Hz1.csv', delimiter=';',skiprows=1,)

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.plot(data[0,:]/4,data[1,:],color='#FF7800')
ax.plot([22.25,22.25],[0,53],linestyle='--')
ax.errorbar(exp[:,0]/2,exp[:,1],xerr=.5,yerr=1,fmt='.',color='#FF7800')
ax.set_ylabel(r'$i_a, \mu A$')
ax.set_xlabel(r'$\varphi_y, V$')
ax.set_ylim(bottom=0)
ax.grid()
plt.savefig('Fr-Hz1.pdf')