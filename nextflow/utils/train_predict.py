import defopt
import random
import json

def sanitize_number(x):
    """Convert x to int if it is a whole number, else leave as float"""
    x = float(x)
    if x.is_integer():
        return str(int(x))
    else:
        return str(x)


def main(*, lon: float, lat: float, seed: int, output: str):
    """
    Pretend to train, predict and select
    @param lon longitude
    @param lat latitude
    @param seed random seed
    @param output output file
    """
    data = {
        'score': random.random(),
    }

    lon_str = sanitize_number(lon)
    lat_str = sanitize_number(lat)
    print(f'writing score in file {output}')
    with open(output, "w") as f:
        json.dump(data, f)


if __name__ == '__main__':
    defopt.run(main)

