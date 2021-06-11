import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import os, sys
import numpy as np

from pylab import rcParams
import matplotlib.pylab as pylab

rcParams['legend.numpoints'] = 1
mpl.style.use('seaborn')
# plt.rcParams['axes.facecolor']='binary'
# print(rcParams.keys())
params = {
    'font.family': 'sans-serif',
    'font.sans-serif': 'Times New Roman',
    'font.weight': 'bold'
}
pylab.rcParams.update(params)

def plot(dataset_name):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6), tight_layout=True)
    # ax = ax.ravel()
    s = ['ResNet18 AUC', 'ResNet50 AUC', 'ResNet18 Accuracy', 'ResNet50 Accuracy']
    title = [dataset_name+' AUC', dataset_name+' Accuracy']

    filename18 = "./data/resnet18_" + dataset_name + ".txt"
    filename50 = "./data/resnet50_" + dataset_name + ".txt"
    data18 = np.loadtxt(filename18,usecols=[1, 2], ndmin=2).T
    data50 = np.loadtxt(filename50,usecols=[1, 2], ndmin=2).T
    n = data18.shape[1]  # number of rows
    x = range(0,n)
    for i in range(2):
        ax[i].plot(x, data18[i], '-', c='#e41b1b', label=s[2*i], linewidth=1.5, markersize=6)
        ax[i].plot(x, data50[i], '-', c='#377eb8', label=s[2*i+1], linewidth=1.5, markersize=6)
        ax[i].set_title(title[i],fontweight='bold',fontsize=16)
        ax[i].legend(loc='best',fancybox=True, framealpha=0,fontsize=14)
        ax[i].grid(True, linestyle='dotted')  # x坐标轴的网格使用主刻度

    plt.savefig(dataset_name+'.png', format='png', dpi=400)
    plt.show()

plot("breast")
plot('chest')
plot('retina')
plot('path')