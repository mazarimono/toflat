import json
import re
from pathlib import Path

import geopandas as gpd
import pytest

from toflat import toflat

p = Path("tests/data")
zips = list(p.glob("*.zip"))


def test_flat_file():
    test_geo = gpd.read_file("toflat/data/jgd2011_plane_rect_crs.geojson")
    tf_file = toflat.ToFlat(zips[0]).flat_file
    assert tf_file.equals(test_geo)


def test_flat_str():
    with pytest.raises(TypeError, match="gdfとして与えられたデータの型がGeoDataFrameではありません"):
        toflat.ToFlat(zips[0]).flat_epsg


def test_epsg():
    d = gpd.read_file("tests/data/P34-14_25_GML.zip", encoding="cp932")
    tf_epsg = toflat.ToFlat(d).flat_epsg
    epsg_int = tf_epsg.split(":")[1]
    pref_num = d.loc[0, "P34_001"][:2]
    geo = gpd.read_file("toflat/data/jgd2011_plane_rect_crs.geojson")
    geo = geo.query(f"EPSGコード == {epsg_int}")
    with open("tests/data/vk_dict.json", "r") as f:
        pref_json = json.load(f)
        pref_name = pref_json[pref_num]
    assert re.search(pref_name, str(geo["適用区域"].values))


def test_to_flat():
    d = gpd.read_file("tests/data/P34-14_25_GML.zip", encoding="cp932")
    tf = toflat.ToFlat(d).to_flat()
    assert tf.crs == "EPSG:6674"


if __name__ == "__main__":
    d = gpd.read_file("toflat/data/jgd2011_plane_rect_crs.geojson", encoding="cp932")
    print(d)
