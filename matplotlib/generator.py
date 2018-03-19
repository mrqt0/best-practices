def generate_logs():
    """
	Generate log files that can be analyzed and plotted.
    """

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