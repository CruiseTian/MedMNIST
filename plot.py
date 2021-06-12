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

    # filename18 = "./data/resnet18_" + dataset_name + ".txt"
    # filename50 = "./data/resnet50_" + dataset_name + ".txt"
    filename18 = "./data/" + dataset_name + "18.txt"
    filename50 = "./data/" + dataset_name + "50.txt"
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

def plot_loss(dataset_name):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6), tight_layout=True)
    # ax = ax.ravel()
    s = ['ResNet18 train loss', 'ResNet18 val loss', 'ResNet50 train loss', 'ResNet50 val loss']
    title = [dataset_name+' 18', dataset_name+' 50']

    # filename18 = "./data/resnet18_" + dataset_name + ".txt"
    # filename50 = "./data/resnet50_" + dataset_name + ".txt"
    train18name = "./data/" + dataset_name + "18_train_loss.txt"
    train50name = "./data/" + dataset_name + "50_train_loss.txt"
    val18name = "./data/" + dataset_name + "18_val_loss.txt"
    val50name = "./data/" + dataset_name + "50_val_loss.txt"
    train18 = np.loadtxt(train18name, ndmin=2)
    train50 = np.loadtxt(train50name, ndmin=2)
    val18 = np.loadtxt(val18name, ndmin=2)
    val50 = np.loadtxt(val50name, ndmin=2)
    n = train18.shape[0]  # number of rows
    x = range(0,n)
    ax[0].plot(x, train18, '-', c='#e41b1b', label=s[0], linewidth=1.5, markersize=6)
    ax[0].plot(x, val18, '-', c='#377eb8', label=s[1], linewidth=1.5, markersize=6)
    ax[0].set_title(title[0],fontweight='bold',fontsize=16)
    ax[0].legend(loc='best',fancybox=True, framealpha=0,fontsize=14)
    ax[0].grid(True, linestyle='dotted')  # x坐标轴的网格使用主刻度

    ax[1].plot(x, train50, '-', c='#e41b1b', label=s[2], linewidth=1.5, markersize=6)
    ax[1].plot(x, val50, '-', c='#377eb8', label=s[3], linewidth=1.5, markersize=6)
    ax[1].set_title(title[1],fontweight='bold',fontsize=16)
    ax[1].legend(loc='best',fancybox=True, framealpha=0,fontsize=14)
    ax[1].grid(True, linestyle='dotted')  # x坐标轴的网格使用主刻度

    plt.savefig(dataset_name+'_loss.png', format='png', dpi=400)
    plt.show()

plot("breast")
plot_loss('breast')
plot('chest')
plot_loss('chest')
plot('retina')
plot_loss('retina')
plot('path')
plot_loss('path')