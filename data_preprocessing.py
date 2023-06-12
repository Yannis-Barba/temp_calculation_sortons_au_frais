import geopandas as gpd

## Bufferize places

print("Bufferize places")

# places = gpd.read_file("./data/biotope.temperature_device.geojson")

# places = places.to_crs(3946)

# places_buffered = places.buffer(30)

# places_buffered.to_file("./data/output/places_buffered.geojson", driver="GeoJSON")


## Convert into GPKG 

print("Convert into GPKG ")
# places_buffered.to_file("./data/output/places_buffered.gpkg", driver="GPKG")

places_buffered_gpkg = gpd.read_file("./data/output/places_buffered.gpkg")

## Clip Other data

print("Clip Other data")

# print("Temp")

# temp = gpd.read_file("./data/raw_data/temp_surface.gpkg")
# temp = temp.to_crs(3946)

# clipped_temp = gpd.clip(temp, places_buffered_gpkg)

# clipped_temp.to_file("./data/output/clipped_temp.gpkg", driver="GPKG", layers="temp")

print("Veget")

veget = gpd.read_file("./data/raw_data/veget_strat.gpkg")
veget = veget.to_crs(3946)

clipped_veget = gpd.clip(veget, places_buffered_gpkg)

clipped_veget.to_file("./data/output/clipped_veget.gpkg", driver="GPKG", layers="veget")

