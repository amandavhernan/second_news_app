import geojson

input_file = 'static/md_zips.geojson'

# Read the input GeoJSON file
with open(input_file, 'r') as f:
    data = geojson.load(f)

# Split the input data and write each boundary to a separate GeoJSON file
for i, feature in enumerate(data['features']):
    zipcode = feature['properties']['ZIPCODE1']
    output_data = geojson.FeatureCollection([feature])
    output_file = f'static/zipcode_{zipcode}.geojson'
    with open(output_file, 'w') as f:
        geojson.dump(output_data, f)