# Nextflow 

## Install Nextflow (if not already)
On Linux/macOS:
```
curl -s https://get.nextflow.io | bash
mv nextflow ~/bin/   # or somewhere in your PATH
```

## Test that nextflow is working

```
nextflow -v
```

## Prepare the folder structure
Make sure your files are organised like this:
```
project/
├─ main.nf                  # the Nextflow pipeline
├─ nextflow.config          # optional, e.g., executor settings
├─ utils/
│  └─ train_predict.py      # your Python script
├─ input/
│  └─ lonlatseed.csv
└─ output/                  # will be created if missing
```

## Run the pipeline locally
From the project directory:
nextflow run main.nf
This will execute the workflow locally. By default:
Each (lon,lat,seed) tuple will run train_predict.py in parallel.
The final CSV lonlatseed.csv will be written in the current working directory.

### Optional: specify parameters
You can override the defaults using --param_name value:
```
nextflow run main.nf \
  --input_csv ../input/lonlatseed.csv \
  --output_dir ../output \
  --num_best 3
```

### Optional: run on a cluster
On a Slurm platform, edit nextflow.config to set the executor:
```
process.executor = 'slurm'  // or 'pbs', 'sge'
process.queue = 'normal'    // optional
```
Then run:
```
nextflow run main.nf
```
Nextflow will automatically submit the train_predict tasks to the cluster.

## Check workflow progress
Nextflow provides a real-time execution log:
nextflow log
nextflow timeline       # generates HTML timeline of tasks
nextflow report         # generates summary report


