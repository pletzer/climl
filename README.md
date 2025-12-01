# climl

Workflow environments to train an ML algorithm for climatology

## Prerequisites

On a local platform:

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Snakemake

```sh
cd snakemake
snakemake --delete-all-output
snakemake -n 
snakemake --core 4
```

## Nextflow

[Install Nextflow](https://www.nextflow.io/docs/latest/install.html)

```sh
nextflow run nextflow
```