
#CODE TAKE FROM: https://matplotlib.org/stable/tutorials/colors/colormaps.html

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
# from colorspacious import cspace_converter



cmaps = {}

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} colormaps', fontsize=14)

    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    # Save colormap list for later.
    cmaps[category] = cmap_list


#EXAMPLE 
plot_color_gradients('Perceptually Uniform Sequential',
                     ['viridis', 'plasma', 'inferno', 'magma', 'cividis'])
plt.show()

#EXAMPLE 
plot_color_gradients('Sequential',
                     ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'])
plt.show()

#EXAMPLE 
plot_color_gradients('Sequential (2)',
                     ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
                      'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
                      'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper'])
plt.show()

#EXAMPLE 
plot_color_gradients(
'Diverging',
['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',
'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'])

plt.show()

           
#EXAMPLE 
plot_color_gradients(
'Qualitative',
['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',
'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b',
'tab20c']
)
plt.show()


#EXAMPLE 
plot_color_gradients(
'Miscellaneous',
['flag', 'prism', 'ocean', 'gist_earth', 'terrain',
'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
'turbo', 'nipy_spectral', 'gist_ncar'])
plt.show()


