import geopandas as gpd
import pkg_resources
from dataclasses import dataclass

FLAT_FILE = pkg_resources.resource_filename(
    'data/jgd2011_plane_rect_crs.geojson'
)

@dataclass
class ToFlat:

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
        union = self.gdf['geometry'].unary_union
        center = union.centroid
        nearest_index = self.s_index.nearest(center)[1]
        epsg_num = self.flat_file.loc[nearest_index[0], 'EPSGコード']
        epsg_str = f'EPSG:{epsg_num}'
        return epsg_str
    

    def to_flat(self) -> gpd.GeoDataFrame:
        flat_df = self.gdf.to_crs(self.flat_epsg)
        return flat_df
    

