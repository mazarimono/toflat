# toflat: Japanese latlon to xy.

toflatは、日本の経度緯度情報を持つGeoDataFrameを、簡単に平面直角座標系（JGD2011）に変換するためのPythonモジュールです。これまでのようにEPSGコードを調べなくても、toflatが調べて、GeoDataFrameにCRSを割り当ててくれます。    
    
toflat is a Python module designed to easily convert GeoDataFrames containing longitude and latitude information of Japan into the plane rectangular coordinate system (JGD2011). Unlike before, there is no need to look up EPSG codes, as toflat does the search and assigns the CRS to the GeoDataFrame for you.    
     
## インストール方法　Install

```
pip install git+https://github.com/mazarimono/toflat.git
```

```
pip install toflat
```

## 使い方 How to Use

```python

from toflat import toflat
data = {
    'name': ['Kyoto Station', 'Kinkaku temple', 'MK bowl', 'Ginaku_temple'],
    'geometry': [point1, point2, point3, point4]
}
gdf = gpd.GeoDataFrame(data, geometry='geometry').set_crs('EPSG:4326')
tf = toflat.ToFlat(gdf)
kyoto_df = tf.to_flat() # CRS EPSG:6674に設定される

```

## License
MIT

