# climl

Workflow environments to train an ML algorithm for climatology

## Prerequisites

On a local platform, 
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Snakemake

```
cd snakemake
snakemake --delete-all-output
snakemake -n 
snakemake --core 4
```



