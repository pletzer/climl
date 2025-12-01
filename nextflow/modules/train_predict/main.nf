process train_predict {
    input:
    tuple val(lat), val(lon), val(seed)

    output:
    path('*.json')

    script:
    """
    train_predict.py --lon ${lon} --lat ${lat} --seed ${seed}
    """
}