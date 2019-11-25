"""
MatrixGraph(data, colticklabels, rowticklabels, collabel, rowlabel, zmin, zmax, zlabel, unit=?, values=False)
TopolopgyGraph(data, x, y, markerlabels, group/split/...)
TopologgyGraph on circle or with certain node in the center?
DeltaTime
"""

import pickle as pl

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use("ggplot")

# def plot_scatter(loss):
#     a = np.zeros((20, 20))
#     with open("link-table.csv") as f:
#         for row, line in enumerate(f):
#             for col, val in enumerate(line.split(";")):
#                 if not val:
#                     continue
#                 a[row][col] = float(val)
#     b = loss
#     fig, ax = plt.subplots()
#     for tx in nodes:
#         if tx in ("SDTR_004", "SDTR_020"): # mobile nodes
#             continue
#         for rx in nodes:
#             if rx in ("SDTR_004", "SDTR_020"): # mobile nodes
#                 continue
#             if tx == rx:
#                 continue
#             ax.scatter(a[stations[tx]-1][stations[rx]-1], b[nodes.index(tx)][nodes.index(rx)], alpha=0.2)
#     ax.set_xlim([0, 100])
#     ax.set_ylim([0, 100])
#     ax.set_xlabel("Link quality from Radio Mobile simulations")
#     ax.set_ylabel("Percent received BFT messages")

def show():
    plt.show()


class LinkMatrix():
    def __init__(self, data, labels, lims=tuple(), name="", unit="%"):
        self.data = data
        if lims:
            self.lims = lims
        else:
            self.lims = (np.nanmin(data), np.nanmax(data))
        self.labels = labels
        self.name = name
        self.unit = unit
        self.cmap = mpl.cm.get_cmap("viridis_r")
        self.norm = mpl.colors.Normalize(self.lims[0], self.lims[1])


    def format(self, value):
        if self.unit == "%":
            return "{:3.0%}".format(value)
        return "{:3.0f}".format(value)


    def plot(self):
        data = self.data
        labels = self.labels
        cmap = self.cmap
        fig, axes = plt.subplots(2, 2,
            gridspec_kw = {'width_ratios': [3, 1], 'height_ratios': [3, 1]})
        self.plot_matrix(data, labels, axes[0][0])
        self.plot_margin_right(data, labels, axes[0][1])
        self.plot_margin_bottom(data, labels, axes[1][0])
        self.plot_summary(data, axes[1][1])
        self.plot_colorbar(fig)

        axes[1][0].get_shared_x_axes().join(axes[0][0], axes[1][0])
        axes[0][1].get_shared_y_axes().join(axes[0][0], axes[0][1])

        # TODO: make save function which guesses filename
        filename = "linkmatrix-{}".format(self.name.lower().replace(" ", "-"))
        plt.savefig(filename + ".png", bbox_inches='tight', dpi=300)
        pl.dump(fig, open(filename + ".fig", "wb"))


    def plot_matrix(self, data, labels, ax):
        ax.matshow(data, cmap=self.cmap, norm=self.norm)
        ax.set_xlabel("Receiver Station")
        ax.xaxis.set_label_position('top')
        ax.xaxis.set_ticks_position('top')
        ax.axis('tight')
        ax.set_ylabel("Transmitter Station")
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=80, family="monospace")
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels, family="monospace")


    def plot_margin_right(self, data, labels, ax):
        sum_x = np.nanmean(data, 1)
        ax.barh(range(len(labels)), sum_x, height=1, color=[self.cmap(self.norm(val)) for val in sum_x])
        ax.margins(0, 0)
        ax.set_xlim(self.lims[0], self.lims[1])
        ax.invert_yaxis()
        ax.set_xticklabels([self.format(x) for x in ax.get_xticks()])
        ax.set_yticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)


    def plot_margin_bottom(self, data, labels, ax):
        sum_y = np.nanmean(data, 0)
        ax.bar(range(len(labels)), sum_y, width=1, color=[self.cmap(self.norm(val)) for val in sum_y])
        ax.margins(0, 0)
        ax.set_ylim(self.lims[1], self.lims[0])
        ax.set_xticks([])
        ax.set_yticklabels([self.format(y) for y in ax.get_yticks()])
        ax.spines["top"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)


    def plot_summary(self, data, ax):
        text = [
            ["min", self.format(np.nanmin(data))],
            ["max", self.format(np.nanmax(data))],
            ["mean", self.format(np.nanmean(data))]
        ]
        ax.table(cellText=text, loc="center")
        ax.axis("off")


    def plot_colorbar(self, fig):
        plt.subplots_adjust(right=0.8)
        ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        sm = plt.cm.ScalarMappable(cmap=self.cmap, norm=self.norm)
        sm.set_array(self.data)
        cbar  = fig.colorbar(sm, cax=ax)
        cbar.ax.set_yticklabels([self.format(self.norm.inverse(y)) for y in ax.get_yticks()])
        cbar.ax.set_ylabel("{} ({})".format(self.name, self.unit))


class LinkTopology():
    def __init__(self, data, test, labels, lims=tuple(), name="", unit="%"):
        self.data = data
        self.test = test
        if lims:
            self.lims = lims
        else:
            self.lims = (np.nanmin(data), np.nanmax(data))
        self.labels = labels
        self.name = name
        self.unit = unit
        self.cmap = mpl.cm.get_cmap("viridis_r")
        self.norm = mpl.colors.Normalize(self.lims[0], self.lims[1])

    def station_to_coord(self, station):
        position = self.test.positions[format(station)]
        x = 0
        y = 0
        for coord in position.split(" ")[:2]:
            deg, m_s_ = coord.split("°")
            m, s_ = m_s_.split("'")
            s, direction = s_.split("\"")
            if direction == "O":
                x = int(deg) + int(m) / 60 + int(s) / 3600
            elif direction == "N":
                y = int(deg) + int(m) / 60 + int(s) / 3600
        return x, y

    def plot_single(self):
        stationary_nodes = self.test.nodes.copy()
        stationary_nodes.remove("SDTR_004")
        stationary_nodes.remove("SDTR_020")
        for tx in stationary_nodes:
            self.plot(transmitters=[tx], receivers=stationary_nodes)
        for rx in stationary_nodes:
            self.plot(transmitters=stationary_nodes, receivers=[rx])

    def plot(self, transmitters=None, receivers=None):
        fig, ax = plt.subplots()
        for station in self.test.stations.values():
            # TODO: plot labels with radio name
            if ".2" in station or station not in self.test.positions:
                continue
            x, y =  self.station_to_coord(station)
            ax.scatter(x, y, color="k")
            ax.annotate(station[8:].split(".")[0], (x, y))

        for tx_idx, tx in enumerate(self.test.nodes):
            if tx not in transmitters:
                continue
            for rx_idx, rx in enumerate(self.test.nodes):
                if rx not in receivers:
                    continue
                xt, yt = self.station_to_coord(self.test.stations[tx])
                xr, yr = self.station_to_coord(self.test.stations[rx])
                z = self.data[tx_idx][rx_idx]
                c = 'k' if np.isnan(z) else self.cmap(self.norm(z))
                a = 0 if np.isnan(z) else 1 - self.norm(z)
                foo = ax.plot([xt, xr], [yt, yr], color=c, alpha=a)

        ax.set_xticks([])
        ax.set_yticks([])

        suffix = "all"
        if len(transmitters) == 1:
            ax.set_title("Transmitter Station {} ({})".format(self.test.stations[transmitters[0]], transmitters[0]))
            suffix = "tx-" + transmitters[0][-2:]
        if len(receivers) == 1:
            ax.set_title("Receiver {}".format(receivers[0]))
            suffix = "rx-" + receivers[0][-2:]

        sm = plt.cm.ScalarMappable(norm=self.norm, cmap=self.cmap)
        sm.set_array([])
        cb = fig.colorbar(sm)
        cb.ax.set_ylabel("{} ({})".format(self.name, self.unit))
        # TODO: savefig as link-bft-packets-received-tx-01
        cb.ax.set_yticklabels(["{:3.0%}".format(self.norm.inverse(y)) for y in cb.ax.get_yticks()])
        filename = "topology-{}-{}".format(self.name.lower().replace(" ", "-"), suffix)
        plt.savefig(filename + ".png", bbox_inches='tight', dpi=300)


def delay_histogram(delay):
    delays = list()
    for line in delay:
        for l in line:
            for val in l:
                delays.append(val)

    print("Min:", min(delays))
    print("Max:", max(delays))
    print("Avg:", np.mean(delays))

    fig, axes = plt.subplots(2, 1, sharex=True)
    axes[0].hist(delays, 100, normed=True)
    axes[1].hist(delays, 100, normed=True, cumulative=True)
    for ax in axes:
        ax.set_xlabel("Delay [s]")
        ax.grid()
    axes[0].set_ylabel("Normed Distribution")
    axes[1].set_ylabel("Cumulative Distribution")
    #axes.set_xlabel("Delay [s]")
    #axes.set_ylabel("Frequency")
    fig.tight_layout()
    fig.savefig("delay-hist.png", bbox_inches='tight', dpi=300)


class TimeDelayGraph():
    def __init__(self):
        """
        Args:
        time: array(tx, seq_no)
        delay: array(tx, rx, seq_no)
        nodes: list(rx) of labels in same order
        find way to make tx-rx-mapping work well (which in same figure?)
        """

    def plot(self, tx_time, delay, nodes, events=list()):
        color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

        transmitters = ["02"]
        receivers = nodes #["01", "03", "06"]

        for tx in transmitters:
            min_ = np.nanmin(delay[nodes.index(tx)])
            max_ = np.nanmax(delay[nodes.index(tx)])
            fig, axes = plt.subplots(1, len(receivers), sharey=True)
            for i, rx in enumerate(receivers):
                ax = axes[i]
                for event in events:
                    c = "0.9" if "0" + rx not in event["radio"] else "r"
                    ax.axhspan(event["start"]/60, event["stop"]/60, facecolor=c)
                for s, t in enumerate(tx_time[nodes.index(tx)]):
                    v = delay[nodes.index(tx)][i][s]
                    ax.plot([0, v], [t/60, (t+v)/60], c=color_cycle[s % len(color_cycle)])
                # ax.set_aspect(60)
                ax.set_xlim([0, max_])
                ax.set_xlabel("{}".format(rx), rotation=0)
                ax.xaxis.set_label_position('top')

            fig.suptitle("Transmitter {}".format(tx))
            axes[0].invert_yaxis()
            axes[0].set_ylabel("Test time (min)")
