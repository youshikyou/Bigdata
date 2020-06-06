import geopandas as gpd
gpd.read_file(filepath)

#create map and plot another map in the same figure
ax = world.plot(figsize=(20,20), color='whitesmoke', linestyle=':', edgecolor='black')
df.plot(ax=ax, markersize=2)

"""
To create a GeoDataFrame from a CSV file, we needed to use both Pandas and GeoPandas:
We begin by creating a DataFrame containing columns with latitude and longitude coordinates.
To convert it to a GeoDataFrame, we use gpd.GeoDataFrame().
The gpd.points_from_xy() function creates Point objects from the latitude and longitude columns.
"""
data_df = pd.read_csv(filepath)
data_geo = gpd.GeoDataFrame(data_df, geometry=gpd.points_from_xy(data_df['longitude'],data_df['lattitude']))
data_geo.crs = {'init': 'epsg:xxxx'}  
