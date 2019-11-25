import json
from pathlib import Path

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

def generate_logs():
    # sinusoidal delay?
    # random init?


    data = dict()

    nodes = ["01", "02"]
    data = dict(zip(nodes, [list() for node in nodes]))
    for tx in nodes:
        for seq_no in range(140):
            tx_time = seq_no * 30
            delay = 200*(1 + np.sin(2*np.pi*seq_no/10))
            data 
            for node in nodes:
                if node == tx:
                    entry = {
                        "type": "tx-event",
                        "timestamp": tx_time,
                        "message-data": {
                            "i": f"{node}",
                            "x": f"{tx_time}",
                            "s": f"{seq_no}",
                            "t": "b",
                        }
                    }
                else:
                    entry = {
                        "type": "rx-event",
                        "timestamp": tx_time + delay,
                        "message-data": {
                            "i": f"{tx}",
                            "x": f"{tx_time}",
                            "s": f"{seq_no}",
                            "t": "b",
                        }
                    }
                data[node].append(entry)
    for node in nodes:
        with open(f"logs/{node}.log", "w") as f:
            for line in data[node]:
                f.write(json.dumps(line))
                f.write("\n")



def read_data():
    tx_events = list()
    rx_events = list()
    for file in Path("logs").glob("*.log"):
        with file.open() as f:
            for line in f:
                entry = json.loads(line)
                if entry["type"] == "tx-event":
                    tx_event = {
                        "tx": entry["message-data"]["i"],
                        "seq-no": entry["message-data"]["s"],
                        "x": entry["message-data"]["x"],
                        "tx-time": entry["timestamp"]
                    }
                    tx_events.append(tx_event)
                else:
                    rx_event = {
                        "tx": entry["message-data"]["i"],
                        "rx": file.name[0:2],
                        "seq-no": entry["message-data"]["s"],
                        "x": entry["message-data"]["x"],
                        "rx-time": entry["timestamp"]
                    }
                    rx_events.append(rx_event)
    tx_df = pd.DataFrame(tx_events)
    rx_df = pd.DataFrame(rx_events)
    data = pd.merge(tx_df, rx_df, on=["tx", "seq-no", "x"])
    return data

def plot(data):
    for tx in ["01", "02"]:
        fig, ax = plt.subplots()
        t = data[data["tx"] == tx]["tx-time"]
        r = data[data["tx"] == tx]["rx-time"]
        ax.scatter(t, r-t)
        ax.set_aspect("equal")
    plt.show()

data = read_data()
plot(data)