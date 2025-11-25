# Snakemake Workflow: Train/Predict and Select Best Scores

This workflow runs utils/train_predict.py for each set of parameters defined in `input/lonlatseed.csv`, 
then collects all results and selects the best 3 scores for each (LON, LAT) pair.

## Input

`input/lonlatseed.csv`
A CSV file containing rows of:
```
LON,LAT,SEED
10,-45,1
10,-45,2
10,-45,3
20,-30,1
20,-30,2
...
```
Each row defines one execution of:
python utils/train_predict.py --lon LON --lat LAT --seed SEED
The script must produce:
```
output/lonLON_latLAT_seedSEED.json
```
Each JSON must contain a field:
```
{"score": <numeric_value>}
```

## Outputs

1. JSON results
Stored in output/:
```
output/lon10_lat-45_seed1.json
output/lon10_lat-45_seed2.json
output/lon10_lat-45_seed3.json
...
```
2. Final aggregated CSV

```
output/lonlatseed.csv
```
This file contains the top 3 scoring SEED values for each (LON, LAT).

## Running the Workflow

1. Run the workflow
To execute all steps:
```
snakemake --cores 4
```
Adjust the number of CPU cores as needed.
2. Dry-run to preview actions
```
snakemake -n
```
This shows what rules would run without actually executing anything.
3. Clean outputs (optional)
```
snakemake --delete-all-output
```

## File Layout Example
```
climl/
│
├── snakefile/Snakefile
├── README.md
├── utils/
│   └── train_predict.py
│
├── input/
│   └── lonlatseed.csv
│
└── output/
    └── (generated files appear here)
```
