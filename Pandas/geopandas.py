import geopandas as gpd
gpd.read_file(filepath)

#create map and plot another map in the same figure
ax = world.plot(figsize=(20,20), color='whitesmoke', linestyle=':', edgecolor='black')
df.plot(ax=ax, markersize=2)
