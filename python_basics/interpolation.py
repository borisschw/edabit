

import percent as bat_pct

def interpolate(top_idx, bottom_idx, volts_to_pct, voltage):
    x1 = volts_to_pct[top_idx][0]
    y1 = volts_to_pct[top_idx][1]
    x2 = volts_to_pct[bottom_idx][0]
    y2 = volts_to_pct[bottom_idx][1]

    slope = ((y1 - y2)) / (x1 - x2)
    est = slope * (voltage - x1) + y1
    return est

def getBatteryPercentage(voltage):
        # get index of the colsest voltage.

        for v in range(len(bat_pct.batteryPercent['LiPo high voltage (4.35V)'])):
            if voltage > bat_pct.batteryPercent['LiPo high voltage (4.35V)'][v][0]:
                index = v
                break



        # index = (next (v for v in range(len(bat_pct.batteryPercent['LiPo high voltage (4.35V)'])) if voltage > bat_pct.batteryPercent['LiPo high voltage (4.35V)'][v][0]))
        pct = interpolate(index-1, index, bat_pct.batteryPercent['LiPo high voltage (4.35V)'], voltage )

        return round(pct, 2)



res={}
res["cell_voltages"] = [4.28875, 4.28875, 4.29125, 4.29000, 4.29125, 4.29125]
print(getBatteryPercentage(sum(res["cell_voltages"])))