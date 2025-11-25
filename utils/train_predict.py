import defopt
import random
import json


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

    output_file = f'../output/lon{lon}_lat{lat}_seed{seed}.json'
    with open(output_file, "w") as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    defopt.run(main)