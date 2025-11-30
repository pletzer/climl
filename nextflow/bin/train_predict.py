#!/usr/bin/env python3

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


def main(*, lon: float, lat: float, seed: int):
    """
    Pretend to train, predict and select
    @param lon longitude
    @param lat latitude
    @param seed random seed
    """
    data = {
        'score': random.random(),
    }

    lon_str = sanitize_number(lon)
    lat_str = sanitize_number(lat)
    output_file = f'lon{lon_str}_lat{lat_str}_seed{seed}.json'
    print(f'writing score in file {output_file}')
    with open(output_file, "w") as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    defopt.run(main)