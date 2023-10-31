import sys
sys.path.append('..')
from pathlib import Path
import toflat.toflat as toflat
import geopandas as gpd



if __name__ == "__main__":
    p = Path("tests/data")
    zips = list(p.glob('*.zip'))

    d = gpd.read_file(zips[0])
    tf = toflat.ToFlat(d)
    print(tf.flat_epsg)

    