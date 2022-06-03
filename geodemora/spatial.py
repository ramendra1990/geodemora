import geopandas as gpd

def nFields(shapeFile):
    """Returns number of fields in a shapefile
    """

    gdf = gpd.read_file(shapeFile)
    return len(gdf.columns)