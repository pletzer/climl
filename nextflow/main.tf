#!/usr/bin/env nextflow
nextflow.enable.dsl=2

/*
 * DSL2 Nextflow pipeline for train_predict + best-score aggregation
 * Works with cleaned CSV (no index column) and multiple seeds
 */

params.input_csv  = "../input/lonlat_clean.csv"   // CSV must have header LON,LAT
params.output_dir = "./output"
params.utils_dir  = "./utils"
params.num_best   = 3

// Ensure output directory exists
new File(params.output_dir).mkdirs()

// ------------------------------------------------------
// Process: train_predict
// Produces JSON output per (lon,lat,seed)
// ------------------------------------------------------
process train_predict {

    tag "${lon}_${lat}_${seed}"

    input:
        tuple val(lon), val(lat), val(seed)

    output:
        path "*.json"

    script:
    """
    python ${params.utils_dir}/train_predict.py \
        --lon ${lon} \
        --lat ${lat} \
        --seed ${seed} \
        --output ${params.output_dir}/lon${lon}_lat${lat}_seed${seed}.json
    """
}

// ------------------------------------------------------
// Process: select_best_scores
// Aggregates top scores into CSV
// ------------------------------------------------------
process select_best_scores {

    tag "aggregate_best_scores"

    input:
        path json_files

    output:
        path "${params.output_dir}/lonlatseed.csv"

    script:
    """
    python - <<'PYTHON_CODE'
import json
import re
from pathlib import Path
import pandas as pd

records = []

for jf in json_files:
    with open(str(jf)) as f:
        data = json.load(f)
    p = Path(jf).stem
    m = re.match(r"lon(?P<lon>-?[\\d\\.]+)_lat(?P<lat>-?[\\d\\.]+)_seed(?P<seed>\\d+)", p)
    if not m:
        raise ValueError(f"Filename {jf} does not match expected pattern")
    lon = float(m.group("lon"))
    lat = float(m.group("lat"))
    seed = int(m.group("seed"))
    records.append({
        "LON": lon,
        "LAT": lat,
        "SEED": seed,
        "SCORE": data["score"]
    })

df = pd.DataFrame(records)
best = df.sort_values("SCORE", ascending=False).groupby(["LON","LAT"]).head(${params.num_best}).reset_index(drop=True)
best.to_csv("${params.output_dir}/lonlatseed.csv", index=False)
PYTHON_CODE
    """
}

// ------------------------------------------------------
// Workflow
// ------------------------------------------------------
workflow {

    // --- Load CSV as channel of [LON,LAT] ---
    Channel.fromPath(params.input_csv)
        .splitCsv(header:true)
        .map { row -> [ row.LON as float, row.LAT as float ] }
        .set { lonlat_ch }

    // Seeds channel
    def seeds = [123, 432, 765]
    Channel.from(seeds).set { seed_ch }

    // Generate all combinations with 'cross'
    lonlat_ch
        .cross(seed_ch)   // produces [ [lon, lat], seed ]
        .map { lonlat, seed -> tuple(lonlat[0], lonlat[1], seed) }
        .set { combos_ch }
    
    // --- Run train_predict ---
    train_predict(combos_ch)

    // --- Collect JSON outputs and aggregate top scores ---
    train_predict.out
        .collect()
        .set { json_ch }

    select_best_scores(json_ch)
}
