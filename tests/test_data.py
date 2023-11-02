
from pathlib import Path
from toflat import toflat
import geopandas as gpd



if __name__ == "__main__":
    p = Path("tests/data")
    zips = list(p.glob('*.zip'))
    print(zips[0])

    d = gpd.read_file(zips[0], encoding='cp932')
    tf = toflat.ToFlat(d)
    print(d.loc[0])
    print(tf.flat_epsg)

    