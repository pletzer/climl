import pandas as pd
import defopt
import numpy as np


def main(*, nlon: int=3, nlat: int=4, output_file: str='../input/lonlat.csv'):
    """
    Generate workflow input file
    @param nlon nonumber of longitudes
    @param nlat number of latitudes
    @param nrun number of runs per (lon, lat)
    @param output_file save data to this file
    """
    xmin, xmax = 0., 360.
    ymin, ymax = -90., 90.

    dx = (xmax - xmin) / (nlon - 1)
    dy = (ymax - ymin) / (nlat - 1)

    ntot = nlon*nlat
    data = {'LON': np.empty((ntot,), float),
            'LAT': np.empty((ntot,), float),
            }
    count = 0
    for j in range(nlat):
        y = ymin + j*dy
        for i in range(nlon):
            x = xmin + i*dx
            data['LON'][count] = x
            data['LAT'][count] = y
            count += 1


    data = pd.DataFrame(data)
    data.to_csv(output_file)

if __name__ == '__main__':
    defopt.run(main)

