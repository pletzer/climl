#!/usr/bin/env python3

import json
from pathlib import Path
import pandas as pd
import re
import sys

inputs = sys.argv[1:]
records = []

# Load all JSON outputs
for jf in inputs:
    with open(jf) as f:
        data = json.load(f)

    # Extract lon, lat, seed from filename
    p = Path(jf).stem   # e.g. "lon10_lat-45_seed123"

    m = re.match(r"lon(?P<lon>-?[\d\.]+)_lat(?P<lat>-?[\d\.]+)_seed(?P<seed>\d+)", p)
    if not m:
        raise ValueError(f"Filename {jf} does not match expected pattern")

    lon = float(m.group("lon"))
    lat = float(m.group("lat"))
    seed = int(m.group("seed"))

    records.append({
        "LON": float(lon),
        "LAT": float(lat),
        "SEED": int(seed),
        "SCORE": data["score"]
    })

df = pd.DataFrame(records)

# Select the best num_best seeds for each (lon,lat)
num_best = 3
best = (
    df.sort_values("SCORE", ascending=False)
        .groupby(["LON", "LAT"])
        .head(num_best)
        .reset_index(drop=True)
)

best.to_csv("lonlatseed.csv", index=False)