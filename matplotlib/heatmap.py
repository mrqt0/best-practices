import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

nodes = {
	"SDTR_001": "Station 1",
	"SDHR_002": "Station 2"
}

# TODO: sort data by station
data = np.array([[1/4, 2/4], [3/4, 4/4]])
sum_y = np.mean(data, 0)
sum_x = np.mean(data, 1)

fig, axes = plt.subplots(2, 2, gridspec_kw = {'width_ratios':[3, 1], 'height_ratios': [3, 1]})
im = axes[0][0].matshow(data)

# add margin densities
# TODO: calculate average loss for transmitter and receiver
# for colors see https://stackoverflow.com/questions/25408393/getting-individual-colors-from-a-color-map-in-matplotlib
cmap = mpl.cm.get_cmap() # todo: scale by limits
axes[0][1].barh([0, 1], sum_x, height=1, color=[cmap(val) for val in sum_x])
axes[0][1].invert_yaxis()
axes[1][0].bar([0, 1], sum_y, width=1, color=[cmap(val) for val in sum_y])
axes[1][0].invert_yaxis()

# 
text = [["min", "foo"], ["max", "bar"]]
axes[1][1].table(cellText=text, loc="center")
axes[1][1].xaxis.set_visible(False)
axes[1][1].yaxis.set_visible(False)

# labels
# TODO: print labels horizontally
axes[0][0].set_xticks(range(len(nodes)))
axes[0][0].set_xticklabels(sorted(nodes, key=lambda x:x[-2:]), rotation=80)
axes[0][0].set_yticks(range(len(nodes)))
axes[0][0].set_yticklabels(sorted(nodes, key=lambda x:x[-2:]))

# todo: add colorbar over total height
plt.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
print(im.properties()['clim'])

fig.colorbar(im, cax=cbar_ax)

#plt.tight_layout()
plt.show()