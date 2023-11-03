from dataclasses import dataclass

import geopandas as gpd
import pkg_resources

FLAT_FILE = pkg_resources.resource_filename(
    "toflat", "data/jgd2011_plane_rect_crs.geojson"
)


@dataclass
class ToFlat:
    '''
    gdfで渡す位置情報に対して、日本の平面直角座標系（JGD2011）を
    選択して設定するクラス。

    '''
    gdf: gpd.GeoDataFrame
    file_path: str = FLAT_FILE

    @property
    def flat_file(self) -> gpd.GeoDataFrame:
        d = gpd.read_file(self.file_path)
        return d

    @property
    def s_index(self) -> gpd.sindex.PyGEOSSTRTreeIndex:
        s_index = self.flat_file.sindex
        return s_index

    @property
    def flat_epsg(self) -> str:
        if not isinstance(self.gdf, gpd.GeoDataFrame):
            raise TypeError("gdfとして与えられたデータの型がGeoDataFrameではありません")
        data = self.gdf.to_crs("EPSG:6668")
        union = data["geometry"].unary_union
        center = union.centroid
        nearest_index = self.s_index.nearest(center)[1]
        epsg_num = self.flat_file.loc[nearest_index[0], "EPSGコード"]
        epsg_str = f"EPSG:{epsg_num}"
        return epsg_str

    def to_flat(self) -> gpd.GeoDataFrame:
        flat_df = self.gdf.to_crs(self.flat_epsg)
        return flat_df


if __name__ == "__main__":
    import sys

    sys.path.append("..")
    test_data_path = "toflat/data/P34-14_01_GML.zip"
    d = gpd.read_file(test_data_path, encoding="cp932")
    tf = ToFlat(d)
    tf_d = tf.to_flat()
    print(tf_d)
    print(tf_d.crs)
