# load libraries and set plot parameters
# import numpy as np
import matplotlib

# plt.rcParams['text.usetex'] = True

label_size = 20
font_size = 20
legend_size = 10

def ticks_size():
    """Size of axes' ticks
    """
    return 8


def axis_lw():
    """Line width of the axes
    """
    return 0.1


def plot_lw():
    """Line width of the plotted curves
    """
    return 1.5


params = {'savefig.dpi': 600,
#               'text.usetex': True,
              'figure.dpi': 600,
              'figure.figsize': [4.667, 3.5],
              'font.size': font_size,
              'axes.labelsize': label_size,
              'axes.titlesize': font_size,
              'axes.linewidth': axis_lw(),
#               'text.fontsize': font_size,
              'xtick.labelsize': ticks_size(),
              'ytick.labelsize': ticks_size(),
              'font.family': 'serif',
              'legend.fontsize': legend_size,
              'lines.markersize': 8,
         'grid.linewidth': 0.2,
         'grid.linestyle': '--',
         'legend.framealpha': 1,
         'legend.frameon': True}

matplotlib.rcParams.update(params)
